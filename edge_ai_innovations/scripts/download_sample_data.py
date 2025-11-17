import os
import urllib.request
from pathlib import Path

def create_sample_dataset():
    print("Creating sample dataset structure...")

    base_dir = Path('../data')
    categories = ['plastic', 'paper', 'glass', 'metal', 'organic']

    for split in ['train', 'val']:
        for category in categories:
            category_path = base_dir / split / category
            category_path.mkdir(parents=True, exist_ok=True)

            readme_path = category_path / 'README.txt'
            with open(readme_path, 'w') as f:
                f.write(f"Place {category} images here for {split} set.\n")
                f.write(f"\nRecommended: 100+ images per category\n")
                f.write(f"Format: JPG, PNG\n")
                f.write(f"Resolution: 224x224 or higher\n")

    print("\nDataset structure created!")
    print("\nNext steps:")
    print("1. Collect or download images of recyclable items")
    print("2. Organize images into the appropriate category folders")
    print("3. Recommended sources:")
    print("   - Kaggle: 'waste classification' datasets")
    print("   - Google Images (with usage rights)")
    print("   - Your own photos")
    print("\nDirectory structure:")
    print("data/")
    print("├── train/")
    for category in categories:
        print(f"│   ├── {category}/")
    print("└── val/")
    for category in categories:
        print(f"    ├── {category}/")

def download_sample_images():
    print("\nNote: This is a placeholder for sample image downloading.")
    print("Please manually add your training images to the data/ directories.")
    print("\nFor a quick start, you can use:")
    print("- TensorFlow Datasets: tfds.load('waste_classification')")
    print("- Kaggle Dataset: www.kaggle.com/techsash/waste-classification-data")

if __name__ == "__main__":
    create_sample_dataset()
    download_sample_images()
