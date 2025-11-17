#!/bin/bash

echo "=========================================="
echo "Edge AI Innovations - Raspberry Pi Setup"
echo "=========================================="
echo ""

echo "Step 1: Updating system packages..."
sudo apt update && sudo apt upgrade -y

echo ""
echo "Step 2: Installing Python dependencies..."
sudo apt install -y python3-pip python3-numpy python3-pillow python3-dev

echo ""
echo "Step 3: Installing TFLite Runtime (lightweight)..."
pip3 install --upgrade pip
pip3 install tflite-runtime

echo ""
echo "Step 4: Creating project directory..."
mkdir -p ~/edge_ai_innovations
cd ~/edge_ai_innovations

echo ""
echo "Step 5: Setting up directory structure..."
mkdir -p models scripts data

echo ""
echo "=========================================="
echo "Setup complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Copy your trained .tflite model to ~/edge_ai_innovations/models/"
echo "2. Copy inference scripts to ~/edge_ai_innovations/scripts/"
echo "3. Test inference:"
echo "   python3 scripts/infer_tflite.py test_image.jpg"
echo ""
echo "Optional: Camera setup"
echo "  sudo apt install python3-picamera"
echo "  Enable camera: sudo raspi-config > Interface Options > Camera"
echo ""
echo "=========================================="
