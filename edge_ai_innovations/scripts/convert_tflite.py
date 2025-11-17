import tensorflow as tf
import os

def convert_to_tflite(model_path='./models/recyclable_classifier.h5',
                      output_path='./models/recyclable_classifier.tflite',
                      quantize=True):
    print(f"Loading model from {model_path}...")
    model = tf.keras.models.load_model(model_path)

    converter = tf.lite.TFLiteConverter.from_keras_model(model)

    if quantize:
        print("Applying quantization...")
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        converter.target_spec.supported_types = [tf.float16]

    print("Converting to TFLite format...")
    tflite_model = converter.convert()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'wb') as f:
        f.write(tflite_model)

    original_size = os.path.getsize(model_path) / 1024
    tflite_size = os.path.getsize(output_path) / 1024

    print(f"Conversion completed!")
    print(f"Original model size: {original_size:.2f} KB")
    print(f"TFLite model size: {tflite_size:.2f} KB")
    print(f"Size reduction: {((original_size - tflite_size) / original_size * 100):.2f}%")
    print(f"Model saved to {output_path}")

def convert_with_full_quantization(model_path='./models/recyclable_classifier.h5',
                                   output_path='./models/recyclable_classifier_quant.tflite',
                                   representative_dataset=None):
    print(f"Loading model from {model_path}...")
    model = tf.keras.models.load_model(model_path)

    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]

    if representative_dataset:
        converter.representative_dataset = representative_dataset
        converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
        converter.inference_input_type = tf.uint8
        converter.inference_output_type = tf.uint8

    print("Converting to fully quantized TFLite format...")
    tflite_model = converter.convert()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'wb') as f:
        f.write(tflite_model)

    print(f"Fully quantized model saved to {output_path}")

if __name__ == "__main__":
    convert_to_tflite(quantize=True)
    print("\nConversion completed successfully!")
