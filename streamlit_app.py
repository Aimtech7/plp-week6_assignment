import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

st.set_page_config(
    page_title="Edge AI Innovations - Analysis Studio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.title("🤖 Edge AI Innovations - Analysis Studio")
st.markdown("**Analyze recyclable items, simulate smart agriculture, and explore edge AI capabilities**")

with st.sidebar:
    st.image("https://via.placeholder.com/200x100?text=Edge+AI", use_column_width=True)
    st.markdown("---")
    analysis_type = st.radio(
        "Choose Analysis Type",
        ["📊 Recyclable Classification", "🌾 Smart Agriculture", "🔬 Quantum AI Simulation", "📈 Model Performance"]
    )
    st.markdown("---")
    st.info("💡 **Tip**: This analysis studio helps you understand edge AI models and their applications.")

if analysis_type == "📊 Recyclable Classification":
    st.header("Recyclable Item Classifier Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Model Configuration")

        model_size = st.slider("Model Size (MB)", 0.5, 5.0, 1.8, 0.1)
        quantization = st.selectbox("Quantization Type", ["Float32", "Float16", "Int8"])
        device = st.selectbox("Target Device", ["Raspberry Pi 4", "Raspberry Pi Zero", "Mobile", "Desktop"])

        col_a, col_b = st.columns(2)
        with col_a:
            image_resolution = st.slider("Image Resolution", 128, 512, 224, 64)
        with col_b:
            batch_size = st.slider("Batch Size", 1, 32, 1)

    with col2:
        st.subheader("Performance Metrics")

        device_specs = {
            "Raspberry Pi 4": {"cpu": "ARM Cortex-A72", "ram": "4GB", "freq": "1.5 GHz"},
            "Raspberry Pi Zero": {"cpu": "ARM1176JZF-S", "ram": "512MB", "freq": "1 GHz"},
            "Mobile": {"cpu": "Snapdragon/Apple", "ram": "4-8GB", "freq": "2.5 GHz"},
            "Desktop": {"cpu": "Intel/AMD", "ram": "16GB", "freq": "3.5 GHz"},
        }

        specs = device_specs[device]
        st.json(specs)

    st.markdown("---")

    col_perf1, col_perf2, col_perf3, col_perf4 = st.columns(4)

    with col_perf1:
        device_factors = {
            "Raspberry Pi 4": 35,
            "Raspberry Pi Zero": 180,
            "Mobile": 25,
            "Desktop": 8,
        }
        inference_time = device_factors[device] * (model_size / 1.8)
        st.metric("Inference Time", f"{inference_time:.0f}ms", "per image")

    with col_perf2:
        power_factors = {
            "Raspberry Pi 4": 3.5,
            "Raspberry Pi Zero": 1.2,
            "Mobile": 2.0,
            "Desktop": 65,
        }
        power = power_factors[device]
        st.metric("Power Consumption", f"{power}W", "estimated")

    with col_perf3:
        throughput = (1000 / inference_time) * batch_size
        st.metric("Throughput", f"{throughput:.1f} img/s", "at batch size")

    with col_perf4:
        reduction = (1 - model_size / 5.0) * 100
        st.metric("Size Reduction", f"{reduction:.0f}%", "vs full model")

    st.markdown("---")
    st.subheader("Classification Results")

    col_upload, col_simulate = st.columns([1, 1])

    with col_upload:
        st.write("**Upload Sample Data**")
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
        if uploaded_file:
            st.success("✅ Image uploaded successfully!")

    with col_simulate:
        st.write("**Simulate Classification**")
        simulate = st.button("🎯 Run Simulation", use_container_width=True)

    if simulate or uploaded_file:
        classes = ["Plastic", "Paper", "Glass", "Metal", "Organic"]
        confidences = np.random.dirichlet(np.ones(5)) * 100

        results_df = pd.DataFrame({
            "Class": classes,
            "Confidence (%)": confidences.round(2)
        }).sort_values("Confidence (%)", ascending=False)

        st.dataframe(results_df, use_container_width=True)

        with st.expander("📊 Detailed Analysis"):
            col_chart1, col_chart2 = st.columns(2)

            with col_chart1:
                st.bar_chart(results_df.set_index("Class")["Confidence (%)"])

            with col_chart2:
                st.write("**Classification Confidence Distribution**")
                top_class = results_df.iloc[0]
                st.success(f"**Predicted Class**: {top_class['Class']}")
                st.info(f"**Confidence**: {top_class['Confidence (%)']:.2f}%")

elif analysis_type == "🌾 Smart Agriculture":
    st.header("AI-IoT Smart Agriculture Simulation")

    col_sensors, col_models = st.columns(2)

    with col_sensors:
        st.subheader("Sensor Readings")

        soil_moisture = st.slider("Soil Moisture (%)", 0, 100, 60, 5)
        temperature = st.slider("Temperature (°C)", 0, 50, 25, 1)
        humidity = st.slider("Humidity (%)", 0, 100, 70, 5)
        ph_level = st.slider("pH Level", 4.0, 9.0, 6.5, 0.1)
        npk_nitrogen = st.slider("Nitrogen (ppm)", 0, 200, 100, 10)
        npk_phosphorus = st.slider("Phosphorus (ppm)", 0, 100, 50, 5)
        npk_potassium = st.slider("Potassium (ppm)", 0, 200, 100, 10)

    with col_models:
        st.subheader("AI Model Predictions")

        sensor_data = {
            "Moisture": soil_moisture,
            "Temperature": temperature,
            "Humidity": humidity,
            "pH": ph_level,
            "N": npk_nitrogen,
            "P": npk_phosphorus,
            "K": npk_potassium,
        }

        disease_risk = abs(50 - soil_moisture) * 0.5 + abs(25 - temperature) * 2
        disease_risk = min(100, max(0, disease_risk))

        irrigation_needed = 100 - soil_moisture

        yield_potential = (soil_moisture / 100) * 50 + (temperature / 50) * 30 + (humidity / 100) * 20

        col_p1, col_p2, col_p3 = st.columns(3)

        with col_p1:
            st.metric("Disease Risk", f"{disease_risk:.1f}%",
                     delta=f"{disease_risk-50:.1f}" if disease_risk > 50 else f"{disease_risk-50:.1f}",
                     delta_color="inverse")

        with col_p2:
            st.metric("Irrigation Needed", f"{irrigation_needed:.1f}%",
                     delta="Water needed" if irrigation_needed > 30 else "Adequate")

        with col_p3:
            st.metric("Yield Potential", f"{yield_potential:.1f}%",
                     delta=f"+{yield_potential-50:.1f}" if yield_potential > 50 else f"{yield_potential-50:.1f}")

    st.markdown("---")

    col_data, col_recs = st.columns([1, 1])

    with col_data:
        st.subheader("Sensor Data Summary")
        sensor_df = pd.DataFrame([sensor_data]).T
        sensor_df.columns = ["Current Value"]
        st.dataframe(sensor_df, use_container_width=True)

    with col_recs:
        st.subheader("AI Recommendations")

        recommendations = []

        if soil_moisture < 40:
            recommendations.append("🚰 **Urgent**: Increase irrigation immediately")
        elif soil_moisture < 60:
            recommendations.append("💧 Monitor moisture levels, prepare irrigation")

        if temperature > 35:
            recommendations.append("🌡️ High temperature alert - ensure ventilation")
        elif temperature < 10:
            recommendations.append("❄️ Low temperature - check heating systems")

        if disease_risk > 70:
            recommendations.append("🦠 **HIGH RISK**: Prepare disease treatment")
        elif disease_risk > 50:
            recommendations.append("⚠️ Monitor closely for disease symptoms")

        if (npk_nitrogen < 80 or npk_phosphorus < 40 or npk_potassium < 80):
            recommendations.append("🌱 Nutrient levels low - consider fertilization")

        if not recommendations:
            recommendations.append("✅ All conditions optimal - continue monitoring")

        for rec in recommendations:
            st.write(rec)

    st.markdown("---")

    st.subheader("Historical Data & Trends")

    days = 30
    dates = [datetime.now() - timedelta(days=x) for x in range(days)]

    historical_data = {
        "Date": dates[::-1],
        "Soil Moisture": np.random.normal(60, 10, days)[::-1],
        "Temperature": np.random.normal(25, 5, days)[::-1],
        "Disease Risk": np.random.normal(40, 15, days)[::-1],
    }

    historical_df = pd.DataFrame(historical_data)

    st.line_chart(historical_df.set_index("Date"))

elif analysis_type == "🔬 Quantum AI Simulation":
    st.header("Quantum AI vs Classical AI Comparison")

    col_problem, col_solver = st.columns(2)

    with col_problem:
        st.subheader("Optimization Problem")
        problem_type = st.selectbox("Problem Type", [
            "Traveling Salesman Problem (TSP)",
            "Portfolio Optimization",
            "Drug Discovery",
            "Logistics Route Planning"
        ])

        problem_size = st.slider("Problem Size", 5, 1000, 100, 10)

        problem_descriptions = {
            "Traveling Salesman Problem (TSP)": "Find shortest route visiting all cities",
            "Portfolio Optimization": "Optimize asset allocation for maximum returns",
            "Drug Discovery": "Find optimal molecular compounds",
            "Logistics Route Planning": "Optimize delivery routes across network"
        }

        st.info(f"**Description**: {problem_descriptions[problem_type]}")

    with col_solver:
        st.subheader("Solver Configuration")
        solver = st.radio("Choose Solver Type", ["Classical AI", "Quantum AI"])

        if solver == "Classical AI":
            algorithm = st.selectbox("Algorithm", [
                "Genetic Algorithm",
                "Simulated Annealing",
                "Branch and Bound",
                "Gradient Descent"
            ])
        else:
            algorithm = st.selectbox("Algorithm", [
                "Quantum Annealing",
                "QAOA (Quantum Approximate Optimization)",
                "VQE (Variational Quantum Eigensolver)",
                "Grover's Algorithm"
            ])

    st.markdown("---")

    if st.button("🚀 Run Simulation", use_container_width=True):
        col_classical, col_quantum = st.columns(2)

        with col_classical:
            st.subheader("Classical AI Results")

            classical_time = problem_size ** 2 * 0.001 + np.random.normal(0, 0.1)
            classical_quality = 100 - (problem_size / 10) + np.random.normal(0, 5)
            classical_quality = max(60, min(100, classical_quality))

            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Execution Time", f"{classical_time:.2f}s")
            with c2:
                st.metric("Solution Quality", f"{classical_quality:.1f}%")
            with c3:
                st.metric("Iterations", f"{int(problem_size * 10)}")

        with col_quantum:
            st.subheader("Quantum AI Results")

            quantum_time = np.log2(problem_size) * 0.01 + np.random.normal(0, 0.05)
            quantum_quality = 95 + np.random.normal(0, 3)
            quantum_quality = max(85, min(100, quantum_quality))

            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Execution Time", f"{quantum_time:.4f}s")
            with c2:
                st.metric("Solution Quality", f"{quantum_quality:.1f}%")
            with c3:
                st.metric("Iterations", f"{int(np.log2(problem_size) * 5)}")

        st.markdown("---")

        col_compare1, col_compare2 = st.columns(2)

        with col_compare1:
            speedup = classical_time / quantum_time
            st.success(f"🚀 **Quantum Speedup**: {speedup:.1f}x faster")

        with col_compare2:
            improvement = quantum_quality - classical_quality
            st.info(f"📈 **Quality Improvement**: {improvement:.1f}% better")

        st.markdown("---")

        st.subheader("Comparison Chart")

        comparison_data = pd.DataFrame({
            "Metric": ["Execution Time (log scale)", "Solution Quality", "Scalability"],
            "Classical AI": [np.log10(classical_time + 1), classical_quality, problem_size / 100],
            "Quantum AI": [np.log10(quantum_time + 1), quantum_quality, problem_size / 10]
        })

        st.bar_chart(comparison_data.set_index("Metric"))

elif analysis_type == "📈 Model Performance":
    st.header("Model Performance & Analytics")

    metric_type = st.selectbox("Select Metric Category", [
        "Inference Performance",
        "Model Accuracy",
        "Resource Utilization",
        "Deployment Cost Analysis"
    ])

    if metric_type == "Inference Performance":
        st.subheader("Inference Speed Across Devices")

        devices = ["Raspberry Pi 4", "Raspberry Pi Zero", "Mobile Phone", "Desktop", "GPU Server"]
        inference_times = [35, 180, 25, 8, 2]
        throughputs = [28, 5, 40, 125, 500]

        col1, col2 = st.columns(2)

        with col1:
            perf_df = pd.DataFrame({
                "Device": devices,
                "Inference Time (ms)": inference_times,
                "Throughput (img/s)": throughputs
            })
            st.dataframe(perf_df, use_container_width=True)

        with col2:
            st.bar_chart(perf_df.set_index("Device")["Inference Time (ms)"])

    elif metric_type == "Model Accuracy":
        st.subheader("Accuracy Metrics by Class")

        accuracy_data = pd.DataFrame({
            "Class": ["Plastic", "Paper", "Glass", "Metal", "Organic"],
            "Accuracy": [94.2, 88.5, 91.3, 89.7, 85.2],
            "Precision": [93.1, 87.2, 90.1, 88.5, 84.0],
            "Recall": [95.5, 89.8, 92.5, 90.9, 86.4]
        })

        st.dataframe(accuracy_data, use_container_width=True)
        st.line_chart(accuracy_data.set_index("Class"))

    elif metric_type == "Resource Utilization":
        st.subheader("Resource Usage During Inference")

        time_points = np.arange(0, 100, 5)
        cpu_usage = 30 + 20 * np.sin(time_points / 10) + np.random.normal(0, 2, len(time_points))
        memory_usage = 40 + 10 * np.cos(time_points / 15) + np.random.normal(0, 1, len(time_points))

        resource_df = pd.DataFrame({
            "Time (s)": time_points,
            "CPU Usage (%)": cpu_usage,
            "Memory Usage (%)": memory_usage
        })

        st.line_chart(resource_df.set_index("Time (s)"))

    else:
        st.subheader("Deployment Cost Analysis")

        cost_data = pd.DataFrame({
            "Platform": ["Raspberry Pi", "Mobile App", "Cloud GPU", "Edge Server"],
            "One-Time Cost ($)": [100, 0, 500, 2000],
            "Monthly Operating ($)": [5, 0.50, 150, 300],
            "Scale Ability": ["Low", "High", "High", "Medium"]
        })

        st.dataframe(cost_data, use_container_width=True)

        col_onetime, col_operating = st.columns(2)

        with col_onetime:
            st.bar_chart(cost_data.set_index("Platform")["One-Time Cost ($)"])

        with col_operating:
            st.bar_chart(cost_data.set_index("Platform")["Monthly Operating ($)"])

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>Edge AI Innovations — Pioneering Tomorrow's AI</strong></p>
    <p>This analysis studio demonstrates the capabilities of edge AI models and their applications.</p>
    <p>📚 <a href='#'>View Documentation</a> | 🐙 <a href='#'>GitHub Repository</a> | 💬 <a href='#'>Community</a></p>
</div>
""", unsafe_allow_html=True)
