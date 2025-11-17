import time
import os
from infer_tflite import run_inference

try:
    from picamera import PiCamera
    CAMERA_TYPE = 'picamera'
    print("Using Raspberry Pi Camera")
except ImportError:
    try:
        import cv2
        CAMERA_TYPE = 'opencv'
        print("Using OpenCV camera (USB webcam)")
    except ImportError:
        print("Error: Neither picamera nor opencv-python is installed")
        print("Install one of:")
        print("  - Raspberry Pi: pip3 install picamera")
        print("  - USB Camera: pip3 install opencv-python")
        exit(1)

class RealTimeClassifier:
    def __init__(self, model_path='../models/recyclable_classifier.tflite',
                 labels_path='../models/class_names.txt',
                 interval=2):
        self.model_path = model_path
        self.labels_path = labels_path
        self.interval = interval
        self.camera = None

    def setup_picamera(self):
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.rotation = 0
        time.sleep(2)

    def setup_opencv_camera(self):
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        time.sleep(2)

    def capture_picamera(self, filename='temp_frame.jpg'):
        self.camera.capture(filename)

    def capture_opencv(self, filename='temp_frame.jpg'):
        ret, frame = self.camera.read()
        if ret:
            cv2.imwrite(filename, frame)

    def run(self):
        print("\n" + "=" * 50)
        print("Real-Time Recyclable Item Classifier")
        print("=" * 50)
        print(f"Model: {self.model_path}")
        print(f"Interval: {self.interval} seconds")
        print("Press Ctrl+C to stop")
        print("=" * 50 + "\n")

        if CAMERA_TYPE == 'picamera':
            self.setup_picamera()
        else:
            self.setup_opencv_camera()

        frame_count = 0

        try:
            while True:
                frame_count += 1
                print(f"\n[Frame {frame_count}] Capturing image...")

                if CAMERA_TYPE == 'picamera':
                    self.capture_picamera()
                else:
                    self.capture_opencv()

                print("Running inference...")
                try:
                    predicted_class, confidence = run_inference(
                        model_path=self.model_path,
                        image_path='temp_frame.jpg',
                        labels_path=self.labels_path
                    )

                    print("\n" + "-" * 50)
                    print(f"CLASSIFICATION: {predicted_class.upper()}")
                    print(f"CONFIDENCE: {confidence:.2f}%")
                    print("-" * 50)

                except Exception as e:
                    print(f"Inference error: {e}")

                time.sleep(self.interval)

        except KeyboardInterrupt:
            print("\n\nStopping classifier...")

        finally:
            if CAMERA_TYPE == 'picamera':
                self.camera.close()
            else:
                self.camera.release()

            if os.path.exists('temp_frame.jpg'):
                os.remove('temp_frame.jpg')

            print("Camera released. Goodbye!")

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Real-time recyclable item classification'
    )
    parser.add_argument(
        '--model',
        default='../models/recyclable_classifier.tflite',
        help='Path to TFLite model'
    )
    parser.add_argument(
        '--labels',
        default='../models/class_names.txt',
        help='Path to class labels file'
    )
    parser.add_argument(
        '--interval',
        type=float,
        default=2.0,
        help='Seconds between classifications'
    )

    args = parser.parse_args()

    classifier = RealTimeClassifier(
        model_path=args.model,
        labels_path=args.labels,
        interval=args.interval
    )

    classifier.run()

if __name__ == "__main__":
    main()
