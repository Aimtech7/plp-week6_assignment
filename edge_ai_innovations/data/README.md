# Dataset Structure

This directory contains the training and validation datasets for the recyclable item classifier.

## Directory Structure

```
data/
├── train/
│   ├── plastic/
│   ├── paper/
│   ├── glass/
│   ├── metal/
│   └── organic/
└── val/
    ├── plastic/
    ├── paper/
    ├── glass/
    ├── metal/
    └── organic/
```

## Dataset Instructions

1. Collect images of recyclable items in the following categories:
   - **Plastic**: bottles, containers, packaging
   - **Paper**: newspapers, cardboard, office paper
   - **Glass**: bottles, jars, containers
   - **Metal**: cans, aluminum foil, metal containers
   - **Organic**: food waste, compostable materials

2. Place training images (70-80%) in `train/<category>/`
3. Place validation images (20-30%) in `val/<category>/`

## Recommended Dataset Sources

- **Kaggle**: Search for "recyclable waste" or "garbage classification" datasets
- **ImageNet**: Subset of relevant categories
- **Custom Collection**: Use your smartphone to capture real-world images

## Image Guidelines

- Format: JPG, PNG
- Resolution: At least 224x224 pixels
- Variety: Different lighting, angles, backgrounds
- Quantity: Minimum 100 images per category for good results
