# Edge AI Innovations - Analysis Studio

A powerful Streamlit application for analyzing edge AI models and simulating smart agriculture systems.

## Features

### 1. Recyclable Classification
- Configure model parameters (size, quantization, target device)
- Simulate image classification inference
- View real-time performance metrics
- Upload and test custom images
- See confidence scores for each recyclable class

**Performance Metrics**:
- Inference time: 8ms - 180ms depending on device
- Supported devices: Raspberry Pi, Mobile, Desktop
- Model quantization: Float32, Float16, Int8

### 2. Smart Agriculture Simulator
- Monitor 7 sensor types: soil moisture, temperature, humidity, pH, NPK levels
- Get AI-powered recommendations
- Track disease risk and irrigation needs
- Predict crop yield potential
- View 30-day historical trends

**Key Metrics**:
- Disease risk prediction
- Irrigation requirement calculation
- Yield potential estimation
- Nutrient level analysis

### 3. Quantum AI Simulation
- Compare classical vs quantum approaches
- Test on various optimization problems:
  - Traveling Salesman Problem (TSP)
  - Portfolio Optimization
  - Drug Discovery
  - Logistics Route Planning
- See speedup metrics and solution quality comparison

**Comparison Metrics**:
- Execution time (log scale)
- Solution quality percentage
- Scalability analysis

### 4. Model Performance Analytics
- Inference performance across devices
- Accuracy metrics by class
- Resource utilization tracking
- Deployment cost analysis

---

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup

1. **Install dependencies**
```bash
pip install -r streamlit_requirements.txt
```

**Or install manually**:
```bash
pip install streamlit pandas numpy pillow
```

2. **Verify installation**
```bash
streamlit --version
```

---

## Running the App

### Option 1: Direct Command
```bash
streamlit run streamlit_app.py
```

### Option 2: With Custom Configuration
```bash
streamlit run streamlit_app.py --logger.level=debug
```

### Option 3: Specify Port
```bash
streamlit run streamlit_app.py --server.port 8502
```

---

## Using the Application

### 1. Recyclable Classification

**Steps**:
1. Select "📊 Recyclable Classification" from the sidebar
2. Configure model parameters:
   - Model Size: 0.5 - 5.0 MB (default: 1.8)
   - Quantization Type: Float32, Float16, Int8
   - Target Device: Pi 4, Pi Zero, Mobile, Desktop
   - Image Resolution: 128 - 512 pixels
   - Batch Size: 1 - 32

3. View real-time performance metrics:
   - Inference time
   - Power consumption
   - Throughput
   - Model size reduction

4. Upload an image or click "Run Simulation" to see predictions
5. View confidence scores for all 5 recyclable classes

### 2. Smart Agriculture

**Steps**:
1. Select "🌾 Smart Agriculture" from the sidebar
2. Adjust sensor readings using sliders:
   - Soil Moisture: 0 - 100%
   - Temperature: 0 - 50°C
   - Humidity: 0 - 100%
   - pH Level: 4.0 - 9.0
   - NPK Levels

3. View AI predictions:
   - Disease Risk (%)
   - Irrigation Needed (%)
   - Yield Potential (%)

4. Read AI recommendations based on current conditions
5. Analyze 30-day historical trends

### 3. Quantum AI Simulation

**Steps**:
1. Select "🔬 Quantum AI Simulation" from the sidebar
2. Choose an optimization problem:
   - Traveling Salesman Problem
   - Portfolio Optimization
   - Drug Discovery
   - Logistics Route Planning

3. Set problem size (5 - 1000 nodes)
4. Select solver type:
   - Classical: Genetic Algorithm, Simulated Annealing, Branch & Bound
   - Quantum: Quantum Annealing, QAOA, VQE, Grover

5. Click "Run Simulation"
6. Compare results:
   - Execution time
   - Solution quality
   - Quantum speedup factor

### 4. Model Performance

**Steps**:
1. Select "📈 Model Performance" from the sidebar
2. Choose metric category:
   - Inference Performance
   - Model Accuracy
   - Resource Utilization
   - Deployment Cost Analysis

3. View comprehensive analytics and charts

---

## Data Visualization

The app includes interactive charts for:
- Bar charts for performance comparison
- Line charts for trend analysis
- Tables for detailed metrics
- Expandable sections for drill-down analysis

---

## Browser Compatibility

Works best on:
- Chrome/Chromium
- Firefox
- Safari
- Edge

---

## Performance Tips

1. **For slow devices**: Use lower image resolution (128px) and smaller batch sizes
2. **For fast inference**: Use larger batch sizes and higher resolution
3. **For mobile**: Consider Float16 quantization
4. **For Raspberry Pi**: Use Int8 quantization for maximum speedup

---

## Troubleshooting

### App won't start
```bash
# Check if streamlit is installed
python -m streamlit --version

# Reinstall if needed
pip install --upgrade streamlit
```

### Slow performance
- Reduce image resolution slider
- Use Int8 quantization
- Close other applications
- Check CPU/memory usage

### Data not persisting
- Note: This version doesn't persist data between sessions
- To add persistence, uncomment Supabase integration code

---

## Advanced Features

### Supabase Integration (Optional)

To enable data persistence with Supabase:

1. Uncomment the Supabase imports in the app
2. Add your Supabase credentials
3. Run with database backend

### Custom Models

To test your own models:
1. Export as TFLite format
2. Update model path in the simulator
3. Adjust class names accordingly

---

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|------------|
| RAM | 4 GB | 8 GB |
| CPU | Intel i5 / Ryzen 5 | Intel i7 / Ryzen 7 |
| Storage | 100 MB | 500 MB |
| Browser | Modern | Chrome/Firefox |

---

## API Reference

### Classification Simulator
```python
# Returns prediction results
inference_time: float  # milliseconds
throughput: float      # images/second
power_usage: float     # watts
predictions: dict      # {class: confidence}
```

### Agriculture Simulator
```python
# Sensor inputs
soil_moisture: float   # 0-100 %
temperature: float     # celsius
humidity: float        # 0-100 %
ph_level: float        # 4.0-9.0
npk_n: float          # ppm
npk_p: float          # ppm
npk_k: float          # ppm

# Outputs
disease_risk: float    # 0-100 %
irrigation_needed: float  # 0-100 %
yield_potential: float # 0-100 %
recommendations: list  # strings
```

---

## Contributing

Found a bug? Have a feature request?
- Open an issue on GitHub
- Submit a pull request
- Email: your.email@example.com

---

## License

MIT License - See LICENSE file in root directory

---

## Support

- 📚 Documentation: See edge_ai_innovations/report/README.md
- 🐙 GitHub: https://github.com/yourusername/edge_ai_innovations
- 💬 Discussions: GitHub Discussions
- 📧 Email: your.email@example.com

---

**Happy Analyzing!**

*Pioneering Tomorrow's AI Innovations*
