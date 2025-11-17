import numpy as np
from PIL import Image
import os

try:
    import tflite_runtime.interpreter as tflite
    print("Using tflite_runtime (optimized for edge devices)")
except ImportError:
    import tensorflow.lite as tflite
    print("Using tensorflow.lite")

def load_labels(label_path='./models/class_names.txt'):
    with open(label_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def preprocess_image(image_path, input_shape):
    img = Image.open(image_path).convert('RGB')
    img = img.resize((input_shape[1], input_shape[2]))
    img_array = np.array(img, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def run_inference(model_path='./models/recyclable_classifier.tflite',
                 image_path='./sample.jpg',
                 labels_path='./models/class_names.txt'):
    print(f"Loading TFLite model from {model_path}...")
    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    print(f"Input shape: {input_details[0]['shape']}")
    print(f"Input type: {input_details[0]['dtype']}")

    print(f"Loading and preprocessing image from {image_path}...")
    input_data = preprocess_image(image_path, input_details[0]['shape'])

    if input_details[0]['dtype'] == np.uint8:
        input_scale, input_zero_point = input_details[0]['quantization']
        input_data = input_data / input_scale + input_zero_point
        input_data = input_data.astype(np.uint8)

    interpreter.set_tensor(input_details[0]['index'], input_data)

    print("Running inference...")
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])

    if output_details[0]['dtype'] == np.uint8:
        output_scale, output_zero_point = output_details[0]['quantization']
        output_data = (output_data.astype(np.float32) - output_zero_point) * output_scale

    labels = load_labels(labels_path)

    predictions = output_data[0]
    top_k = 3
    top_k_indices = np.argsort(predictions)[-top_k:][::-1]

    print("\nPredictions:")
    print("-" * 40)
    for i, idx in enumerate(top_k_indices, 1):
        print(f"{i}. {labels[idx]}: {predictions[idx] * 100:.2f}%")

    predicted_class = labels[np.argmax(predictions)]
    confidence = np.max(predictions) * 100

    print("\n" + "=" * 40)
    print(f"RESULT: {predicted_class} ({confidence:.2f}% confidence)")
    print("=" * 40)

    return predicted_class, confidence

def batch_inference(model_path='./models/recyclable_classifier.tflite',
                   image_dir='./test_images',
                   labels_path='./models/class_names.txt'):
    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    labels = load_labels(labels_path)

    results = []

    for image_file in os.listdir(image_dir):
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_dir, image_file)

            input_data = preprocess_image(image_path, input_details[0]['shape'])

            if input_details[0]['dtype'] == np.uint8:
                input_scale, input_zero_point = input_details[0]['quantization']
                input_data = input_data / input_scale + input_zero_point
                input_data = input_data.astype(np.uint8)

            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()
            output_data = interpreter.get_tensor(output_details[0]['index'])

            if output_details[0]['dtype'] == np.uint8:
                output_scale, output_zero_point = output_details[0]['quantization']
                output_data = (output_data.astype(np.float32) - output_zero_point) * output_scale

            predictions = output_data[0]
            predicted_class = labels[np.argmax(predictions)]
            confidence = np.max(predictions) * 100

            results.append({
                'image': image_file,
                'class': predicted_class,
                'confidence': confidence
            })

            print(f"{image_file}: {predicted_class} ({confidence:.2f}%)")

    return results

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        run_inference(image_path=image_path)
    else:
        print("Usage: python infer_tflite.py <image_path>")
        print("Example: python infer_tflite.py ./sample.jpg")
