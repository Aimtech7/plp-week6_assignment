# Quick Start Guide

Get started with Edge AI Innovations in 5 minutes!

## Option 1: Google Colab (Fastest)

1. Upload notebook to Google Colab
2. Run all cells in `notebooks/train.ipynb`
3. Download the trained `.tflite` model

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/edge_ai_innovations/blob/main/notebooks/train.ipynb)

## Option 2: Local Training

### Prerequisites
- Python 3.8+
- 4GB+ RAM
- 2GB disk space

### Installation (5 minutes)

```bash
# Clone repository
git clone https://github.com/yourusername/edge_ai_innovations.git
cd edge_ai_innovations

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Prepare Sample Data (2 minutes)

```bash
# Create directory structure
python scripts/download_sample_data.py

# Add your images to:
# data/train/plastic/
# data/train/paper/
# data/train/glass/
# data/train/metal/
# data/train/organic/
```

**Quick tip**: Need sample data? Download from [Kaggle Waste Classification](https://www.kaggle.com/techsash/waste-classification-data)

### Train Model (10-30 minutes)

**Interactive (recommended for first-time users):**
```bash
jupyter notebook notebooks/train.ipynb
```

**Command line (for production):**
```bash
python scripts/train.py
```

### Convert to TFLite (1 minute)

```bash
python scripts/convert_tflite.py
```

### Test Inference (instant)

```bash
python scripts/infer_tflite.py path/to/test_image.jpg
```

Expected output:
```
RESULT: plastic (94.32% confidence)
```

## Option 3: Raspberry Pi Deployment

### Prerequisites
- Raspberry Pi 4 (2GB+ RAM)
- Raspberry Pi Camera or USB webcam
- MicroSD card (16GB+) with Raspberry Pi OS

### Setup (10 minutes)

```bash
# SSH into your Raspberry Pi
ssh pi@raspberrypi.local

# Download and run setup script
wget https://raw.githubusercontent.com/yourusername/edge_ai_innovations/main/scripts/raspberry_pi_setup.sh
chmod +x raspberry_pi_setup.sh
./raspberry_pi_setup.sh
```

### Transfer Model

```bash
# From your local machine:
scp models/recyclable_classifier.tflite pi@raspberrypi.local:~/edge_ai_innovations/models/
scp models/class_names.txt pi@raspberrypi.local:~/edge_ai_innovations/models/
scp scripts/infer_tflite.py pi@raspberrypi.local:~/edge_ai_innovations/scripts/
```

### Run Real-Time Classification

```bash
# On Raspberry Pi:
cd ~/edge_ai_innovations
python3 scripts/realtime_camera.py
```

## Troubleshooting

### Issue: "No module named tensorflow"
**Solution**: `pip install tensorflow>=2.13.0`

### Issue: "Not enough training data"
**Solution**: Ensure at least 50 images per category. Download sample dataset from Kaggle.

### Issue: Raspberry Pi inference too slow
**Solution**:
- Use quantized model (already done by `convert_tflite.py`)
- Reduce image resolution
- Use Raspberry Pi 4 (recommended)

### Issue: Camera not detected on Raspberry Pi
**Solution**:
```bash
sudo raspi-config
# Navigate to: Interface Options > Camera > Enable
sudo reboot
```

## Next Steps

1. **Improve Model**: Collect more training data for better accuracy
2. **Deploy**: Set up automated system (e.g., smart recycling bin)
3. **Customize**: Modify classes for your specific use case
4. **Contribute**: Share improvements via pull request

## Resources

- Full Documentation: [report/README.md](report/README.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)
- Issues: [GitHub Issues](https://github.com/yourusername/edge_ai_innovations/issues)

## Need Help?

- Check [report/README.md](report/README.md) for detailed documentation
- Open an issue on GitHub
- Email: your.email@example.com

---

**Time to first inference**: ~20 minutes (with sample data)

Happy coding! 🚀
