# Getting Started - Edge AI Innovations

## Quick Overview

This project includes two applications:

1. **React Web App** - Beautiful showcase of Edge AI innovations
2. **Streamlit Analysis Studio** - Interactive data analysis and simulation

---

## Part 1: React Web Application

### View in Browser

The React app is built and ready to preview. Click the "Get Started" button to learn about the Analysis Studio.

**Features:**
- Professional landing page
- Interactive tabs showcasing:
  - TensorFlow Lite Edge AI prototype
  - Key features and specs
  - Smart Agriculture system
  - Quantum AI vs Classical AI comparison
- Responsive design (mobile-friendly)
- Call-to-action sections
- Comprehensive footer

---

## Part 2: Streamlit Analysis Studio

### Installation & Running

#### Step 1: Install Dependencies
```bash
pip install -r streamlit_requirements.txt
```

#### Step 2: Run the Application
```bash
streamlit run streamlit_app.py
```

#### Step 3: Open in Browser
```
http://localhost:8501
```

### What You Can Do

#### 1. Recyclable Classification
- **Adjust model parameters**: Size, quantization, target device
- **View performance metrics**: Inference time, power usage, throughput
- **Simulate predictions**: See confidence scores for 5 recyclable classes
- **Upload images**: Test with custom images

#### 2. Smart Agriculture Simulator
- **Monitor sensors**: 7 types of sensors (moisture, temp, pH, NPK, light, cameras, weather)
- **Get recommendations**: AI-powered suggestions based on sensor data
- **Predict outcomes**: Disease risk, irrigation needs, yield potential
- **Analyze trends**: 30-day historical data visualization

#### 3. Quantum AI Comparison
- **Choose problem type**: TSP, Portfolio, Drug Discovery, Logistics
- **Select solver**: Classical algorithms vs Quantum approaches
- **Run simulation**: See real-time comparison
- **View metrics**: Speedup factor and solution quality

#### 4. Model Performance Analytics
- **Inference speed**: Across different devices
- **Accuracy metrics**: By class and overall performance
- **Resource usage**: CPU, memory during inference
- **Cost analysis**: Deployment costs across platforms

---

## Project Structure

```
project/
├── src/
│   ├── App.tsx              # React main app
│   ├── main.tsx
│   └── index.css
├── dist/                    # Built React app
├── edge_ai_innovations/     # TensorFlow Lite project
│   ├── notebooks/
│   ├── scripts/
│   ├── data/
│   ├── models/
│   └── report/
├── streamlit_app.py         # Streamlit analysis studio
├── streamlit_requirements.txt
├── STREAMLIT_README.md      # Detailed Streamlit docs
└── package.json
```

---

## Key Features

### React App
✅ Professional UI with gradient design
✅ Interactive tab system
✅ Responsive mobile layout
✅ Smooth animations
✅ Call-to-action modals
✅ Beautiful footer

### Streamlit App
✅ Real-time data analysis
✅ Interactive sliders and controls
✅ Performance metric calculations
✅ Chart visualizations
✅ AI recommendations
✅ Multi-tab interface

---

## Technology Stack

### Frontend
- React 18
- TypeScript
- Tailwind CSS
- Vite
- Lucide React (icons)

### Backend Analysis
- Streamlit
- Pandas
- NumPy
- Python 3.8+

### AI/ML Components
- TensorFlow 2.x
- TensorFlow Lite
- Quantization support
- Edge optimization

---

## File Descriptions

### React App Files
- **src/App.tsx**: Main React component with all sections
- **index.html**: HTML entry point
- **tailwind.config.js**: Tailwind CSS configuration
- **vite.config.ts**: Vite build configuration

### Streamlit App Files
- **streamlit_app.py**: Main Streamlit application (800+ lines)
- **streamlit_requirements.txt**: Python dependencies

### Edge AI Project
- **edge_ai_innovations/README.md**: Full project documentation
- **edge_ai_innovations/scripts/**: Training and inference scripts
- **edge_ai_innovations/notebooks/**: Jupyter training notebook
- **edge_ai_innovations/report/**: Comprehensive technical report

---

## Common Tasks

### Edit React App
```bash
# Make changes to src/App.tsx
# Build will auto-reload in preview
npm run build
```

### Add Streamlit Features
```bash
# Edit streamlit_app.py
# Refresh browser to see changes (Streamlit auto-reloads)
```

### Test Edge AI Model
```bash
cd edge_ai_innovations
python scripts/train.py          # Train model
python scripts/convert_tflite.py # Convert to TFLite
python scripts/infer_tflite.py   # Run inference
```

### Deploy to Raspberry Pi
```bash
bash edge_ai_innovations/scripts/raspberry_pi_setup.sh
scp edge_ai_innovations/models/*.tflite pi@raspberrypi:/path/to/models/
```

---

## Performance Metrics

### React App
- Bundle size: 165 KB (gzipped: 51 KB)
- Build time: ~6 seconds
- Fully responsive (mobile to desktop)
- Production-ready

### Streamlit App
- Startup time: ~5 seconds
- Real-time updates: <1 second
- Supports concurrent users
- No backend required

### Edge AI Models
- Model size: <2 MB
- Inference time: 8-180ms (device dependent)
- Accuracy: 85-95%
- Power consumption: <5W

---

## Troubleshooting

### React App Issues
```bash
# Clear cache and rebuild
rm -rf dist node_modules
npm install
npm run build
```

### Streamlit App Issues
```bash
# Clear Streamlit cache
streamlit cache clear
streamlit run streamlit_app.py

# Check Python version
python --version  # Should be 3.8+
```

### Port Already in Use
```bash
# Streamlit uses port 8501 by default
streamlit run streamlit_app.py --server.port 8502
```

---

## Next Steps

1. **View the React App**: Open the preview panel to see the beautiful landing page
2. **Click "Get Started"**: See the Analysis Studio modal with instructions
3. **Run Streamlit Locally**:
   ```bash
   pip install -r streamlit_requirements.txt
   streamlit run streamlit_app.py
   ```
4. **Explore Edge AI Project**: Check `edge_ai_innovations/` for ML models and scripts
5. **Read Documentation**: See `edge_ai_innovations/report/README.md` for comprehensive guide

---

## Learning Resources

- **React App Structure**: Interactive UI showcasing project features
- **Streamlit Simulations**: Hands-on experimentation with AI models
- **Edge AI Project**: Complete ML implementation with training/deployment
- **Documentation**: Theoretical foundations and practical guides

---

## Support & Contributions

- 📚 **Documentation**: `edge_ai_innovations/report/README.md`
- 🐙 **GitHub**: https://github.com/yourusername/edge_ai_innovations
- 💬 **Questions**: Open an issue on GitHub
- 🤝 **Contribute**: Follow guidelines in `CONTRIBUTING.md`

---

## License

MIT License - See `LICENSE` file

---

**You're all set! Explore the Edge AI Innovations project.**

🚀 *Pioneering Tomorrow's AI Innovations*
