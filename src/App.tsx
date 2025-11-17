import { useState } from 'react';
import { Menu, X, ArrowRight, Cpu, Leaf, Zap, Code2, GitBranch, BookOpen } from 'lucide-react';

export default function App() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [activeTab, setActiveTab] = useState('overview');
  const [showStreamlitInfo, setShowStreamlitInfo] = useState(false);

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white">
      {/* Navigation */}
      <nav className="fixed w-full top-0 z-50 bg-slate-900/80 backdrop-blur-md border-b border-slate-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center gap-3">
              <Cpu className="w-8 h-8 text-blue-400" />
              <span className="text-xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
                Edge AI
              </span>
            </div>

            <div className="hidden md:flex items-center gap-8">
              <a href="#features" className="hover:text-blue-400 transition">Features</a>
              <a href="#agriculture" className="hover:text-blue-400 transition">Agriculture</a>
              <a href="#docs" className="hover:text-blue-400 transition">Documentation</a>
              <a href="https://github.com" className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-lg transition">GitHub</a>
            </div>

            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="md:hidden"
            >
              {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>

          {mobileMenuOpen && (
            <div className="md:hidden pb-4 space-y-3">
              <a href="#features" className="block hover:text-blue-400">Features</a>
              <a href="#agriculture" className="block hover:text-blue-400">Agriculture</a>
              <a href="#docs" className="block hover:text-blue-400">Documentation</a>
            </div>
          )}
        </div>
      </nav>

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-4">
        <div className="max-w-6xl mx-auto text-center">
          <div className="mb-8 inline-block">
            <span className="px-4 py-2 rounded-full bg-blue-500/10 border border-blue-500/30 text-blue-300 text-sm font-medium">
              Pioneering Tomorrow's AI Innovations
            </span>
          </div>

          <h1 className="text-5xl md:text-7xl font-bold mb-6 leading-tight">
            Edge AI at the
            <span className="bg-gradient-to-r from-blue-400 via-cyan-400 to-blue-500 bg-clip-text text-transparent"> Edge</span>
          </h1>

          <p className="text-xl text-slate-300 mb-8 max-w-3xl mx-auto leading-relaxed">
            Deploy intelligent AI models on edge devices for real-time inference without cloud latency. Reduce response times, enhance privacy, and enable autonomous decision-making.
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button
              onClick={() => setShowStreamlitInfo(true)}
              className="px-8 py-3 bg-blue-600 hover:bg-blue-700 rounded-lg font-semibold transition flex items-center justify-center gap-2">
              Get Started <ArrowRight size={20} />
            </button>
            <button className="px-8 py-3 border border-slate-600 hover:border-blue-400 rounded-lg font-semibold transition">
              View Documentation
            </button>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-16 px-4 bg-slate-800/40">
        <div className="max-w-6xl mx-auto grid md:grid-cols-4 gap-8">
          <div className="text-center">
            <div className="text-4xl font-bold text-blue-400 mb-2">2000+</div>
            <p className="text-slate-300">Lines of Code</p>
          </div>
          <div className="text-center">
            <div className="text-4xl font-bold text-cyan-400 mb-2">7</div>
            <p className="text-slate-300">Python Scripts</p>
          </div>
          <div className="text-center">
            <div className="text-4xl font-bold text-blue-400 mb-2">35ms</div>
            <p className="text-slate-300">Inference Time</p>
          </div>
          <div className="text-center">
            <div className="text-4xl font-bold text-cyan-400 mb-2">&lt;2MB</div>
            <p className="text-slate-300">Model Size</p>
          </div>
        </div>
      </section>

      {/* Main Content Section */}
      <section className="py-20 px-4">
        <div className="max-w-6xl mx-auto">
          {/* Tabs */}
          <div className="flex flex-wrap gap-4 mb-12 justify-center">
            {[
              { id: 'overview', label: 'Overview', icon: <Code2 size={18} /> },
              { id: 'features', label: 'Features', icon: <Zap size={18} /> },
              { id: 'agriculture', label: 'Smart Agriculture', icon: <Leaf size={18} /> },
              { id: 'quantum', label: 'Quantum AI', icon: <Cpu size={18} /> },
            ].map(tab => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`px-6 py-3 rounded-lg font-semibold transition flex items-center gap-2 ${
                  activeTab === tab.id
                    ? 'bg-blue-600 text-white'
                    : 'bg-slate-700/50 hover:bg-slate-700 text-slate-300'
                }`}
              >
                {tab.icon}
                {tab.label}
              </button>
            ))}
          </div>

          {/* Tab Content */}
          <div className="bg-slate-800/50 rounded-xl p-8 border border-slate-700">
            {activeTab === 'overview' && (
              <div className="space-y-6">
                <h2 className="text-3xl font-bold">TensorFlow Lite Edge AI</h2>
                <p className="text-slate-300 text-lg leading-relaxed">
                  A lightweight image classification model trained to recognize recyclable items in real-time. The model is optimized for edge devices like Raspberry Pi, achieving <span className="text-blue-400 font-semibold">35ms inference time</span> with less than 2MB footprint.
                </p>
                <div className="grid md:grid-cols-2 gap-6 mt-8">
                  <div className="bg-slate-700/50 p-6 rounded-lg border border-slate-600">
                    <h3 className="font-semibold text-blue-400 mb-3">5 Recyclable Classes</h3>
                    <ul className="space-y-2 text-slate-300">
                      <li>• Plastic bottles & containers</li>
                      <li>• Paper & cardboard</li>
                      <li>• Glass jars & bottles</li>
                      <li>• Metal cans</li>
                      <li>• Organic waste</li>
                    </ul>
                  </div>
                  <div className="bg-slate-700/50 p-6 rounded-lg border border-slate-600">
                    <h3 className="font-semibold text-cyan-400 mb-3">Deployment Options</h3>
                    <ul className="space-y-2 text-slate-300">
                      <li>• Raspberry Pi 4/Zero</li>
                      <li>• Mobile devices (Android/iOS)</li>
                      <li>• Google Colab</li>
                      <li>• Desktop/Laptop</li>
                      <li>• Microcontrollers</li>
                    </ul>
                  </div>
                </div>
              </div>
            )}

            {activeTab === 'features' && (
              <div className="space-y-6">
                <h2 className="text-3xl font-bold">Key Features</h2>
                <div className="grid md:grid-cols-2 gap-6">
                  {[
                    { title: 'Real-Time Inference', desc: 'Process images in 10-50ms on edge devices' },
                    { title: 'Model Quantization', desc: 'Float16 quantization reduces model size by 50%' },
                    { title: 'Privacy First', desc: 'All processing happens on-device, no data transmission' },
                    { title: 'Low Power', desc: 'Runs on <5W power consumption' },
                    { title: 'Open Source', desc: 'MIT Licensed, community-driven development' },
                    { title: 'Easy Deployment', desc: 'Automated scripts for Raspberry Pi setup' },
                  ].map((feature, idx) => (
                    <div key={idx} className="bg-slate-700/50 p-6 rounded-lg border border-slate-600 hover:border-blue-500/50 transition">
                      <h3 className="font-semibold text-blue-400 mb-2">{feature.title}</h3>
                      <p className="text-slate-400">{feature.desc}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {activeTab === 'agriculture' && (
              <div className="space-y-6">
                <h2 className="text-3xl font-bold">AI-IoT Smart Agriculture</h2>
                <p className="text-slate-300 text-lg">
                  A conceptual framework integrating IoT sensors with edge AI for precision farming optimization.
                </p>
                <div className="bg-slate-700/30 p-6 rounded-lg border border-slate-600 my-6">
                  <h3 className="font-semibold text-cyan-400 mb-4 text-lg">System Components</h3>
                  <div className="space-y-4">
                    <div>
                      <p className="font-semibold text-blue-400">Sensors (7 types)</p>
                      <p className="text-slate-400 text-sm">Soil moisture, temperature, pH, NPK, light, cameras, weather</p>
                    </div>
                    <div>
                      <p className="font-semibold text-blue-400">Edge AI Models</p>
                      <p className="text-slate-400 text-sm">Disease detection, pest identification, yield prediction, irrigation optimization</p>
                    </div>
                    <div>
                      <p className="font-semibold text-blue-400">Measured Benefits</p>
                      <p className="text-slate-400 text-sm">30-50% water savings • 20-40% yield increase • 60-80% labor reduction</p>
                    </div>
                  </div>
                </div>
                <div className="grid md:grid-cols-3 gap-4">
                  <div className="text-center p-4 bg-slate-700/50 rounded-lg">
                    <div className="text-2xl font-bold text-blue-400">30-50%</div>
                    <p className="text-slate-400 text-sm">Water Savings</p>
                  </div>
                  <div className="text-center p-4 bg-slate-700/50 rounded-lg">
                    <div className="text-2xl font-bold text-cyan-400">20-40%</div>
                    <p className="text-slate-400 text-sm">Yield Increase</p>
                  </div>
                  <div className="text-center p-4 bg-slate-700/50 rounded-lg">
                    <div className="text-2xl font-bold text-blue-400">60-80%</div>
                    <p className="text-slate-400 text-sm">Labor Reduction</p>
                  </div>
                </div>
              </div>
            )}

            {activeTab === 'quantum' && (
              <div className="space-y-6">
                <h2 className="text-3xl font-bold">Quantum AI vs Classical AI</h2>
                <div className="overflow-x-auto">
                  <table className="w-full text-sm">
                    <thead>
                      <tr className="border-b border-slate-600">
                        <th className="text-left py-3 px-4 text-blue-400 font-semibold">Aspect</th>
                        <th className="text-left py-3 px-4 text-blue-400 font-semibold">Classical AI</th>
                        <th className="text-left py-3 px-4 text-cyan-400 font-semibold">Quantum AI</th>
                      </tr>
                    </thead>
                    <tbody className="space-y-2">
                      <tr className="border-b border-slate-700">
                        <td className="py-3 px-4">Processing</td>
                        <td className="py-3 px-4 text-slate-300">Sequential/Limited Parallel</td>
                        <td className="py-3 px-4 text-slate-300">Massive Parallelism</td>
                      </tr>
                      <tr className="border-b border-slate-700">
                        <td className="py-3 px-4">Problem Size</td>
                        <td className="py-3 px-4 text-slate-300">~1000 variables</td>
                        <td className="py-3 px-4 text-slate-300">Exponentially Larger</td>
                      </tr>
                      <tr className="border-b border-slate-700">
                        <td className="py-3 px-4">Speed</td>
                        <td className="py-3 px-4 text-slate-300">Polynomial/Exponential</td>
                        <td className="py-3 px-4 text-slate-300">Quantum Speedup</td>
                      </tr>
                      <tr className="border-b border-slate-700">
                        <td className="py-3 px-4">Maturity</td>
                        <td className="py-3 px-4 text-slate-300">Production-Ready</td>
                        <td className="py-3 px-4 text-slate-300">Research Stage</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <div className="mt-8">
                  <h3 className="font-semibold text-blue-400 mb-4">6 Industries Benefiting from Quantum AI</h3>
                  <div className="grid md:grid-cols-2 gap-4">
                    {[
                      { industry: 'Pharmaceuticals', impact: 'Drug discovery: 10+ years → 2-3 years' },
                      { industry: 'Finance', impact: 'Portfolio optimization for trillion-dollar assets' },
                      { industry: 'Logistics', impact: 'DHL: 30% reduction in delivery costs' },
                      { industry: 'Energy', impact: 'Accelerated clean technology development' },
                      { industry: 'Materials Science', impact: 'Revolutionary batteries & solar cells' },
                      { industry: 'Cryptography', impact: 'Quantum-resistant encryption development' },
                    ].map((item, idx) => (
                      <div key={idx} className="bg-slate-700/50 p-4 rounded-lg border border-slate-600">
                        <p className="font-semibold text-blue-400">{item.industry}</p>
                        <p className="text-slate-400 text-sm mt-1">{item.impact}</p>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </section>

      {/* Call to Action */}
      <section className="py-20 px-4 bg-gradient-to-r from-blue-600/20 to-cyan-600/20 border-y border-slate-700">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-6">Ready to Deploy Edge AI?</h2>
          <p className="text-xl text-slate-300 mb-8">
            Get started with our comprehensive documentation, production-ready code, and automated deployment scripts.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <a href="https://github.com" className="px-8 py-3 bg-blue-600 hover:bg-blue-700 rounded-lg font-semibold transition inline-flex items-center justify-center gap-2">
              <GitBranch size={20} />
              View on GitHub
            </a>
            <a href="#" className="px-8 py-3 border border-slate-600 hover:border-blue-400 rounded-lg font-semibold transition inline-flex items-center justify-center gap-2">
              <BookOpen size={20} />
              Read Docs
            </a>
          </div>
        </div>
      </section>

      {/* Streamlit Info Modal */}
      {showStreamlitInfo && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
          <div className="bg-slate-800 rounded-xl p-8 max-w-2xl w-full border border-slate-700 max-h-96 overflow-y-auto">
            <div className="flex justify-between items-start mb-6">
              <div>
                <h2 className="text-3xl font-bold mb-2">Launch Analysis Studio</h2>
                <p className="text-slate-300">Interactive data analysis powered by Streamlit</p>
              </div>
              <button
                onClick={() => setShowStreamlitInfo(false)}
                className="text-slate-400 hover:text-white"
              >
                <X size={24} />
              </button>
            </div>

            <div className="space-y-6">
              <div className="bg-slate-700/50 p-6 rounded-lg border border-slate-600">
                <h3 className="font-semibold text-blue-400 mb-3 flex items-center gap-2">
                  <Cpu size={20} />
                  Recyclable Classification
                </h3>
                <p className="text-slate-300 text-sm">Analyze recyclable items with real-time classification. Adjust model parameters and simulate predictions.</p>
              </div>

              <div className="bg-slate-700/50 p-6 rounded-lg border border-slate-600">
                <h3 className="font-semibold text-green-400 mb-3 flex items-center gap-2">
                  <Leaf size={20} />
                  Smart Agriculture Simulator
                </h3>
                <p className="text-slate-300 text-sm">Monitor sensor data, get AI recommendations, and visualize crop health predictions.</p>
              </div>

              <div className="bg-slate-700/50 p-6 rounded-lg border border-slate-600">
                <h3 className="font-semibold text-purple-400 mb-3 flex items-center gap-2">
                  <Zap size={20} />
                  Quantum AI Simulation
                </h3>
                <p className="text-slate-300 text-sm">Compare classical vs quantum computing approaches to optimization problems.</p>
              </div>

              <div className="bg-slate-700/50 p-6 rounded-lg border border-slate-600">
                <h3 className="font-semibold text-cyan-400 mb-3 flex items-center gap-2">
                  <Code2 size={20} />
                  Performance Analytics
                </h3>
                <p className="text-slate-300 text-sm">Explore model performance metrics, accuracy data, and deployment cost analysis.</p>
              </div>
            </div>

            <div className="mt-8 p-4 bg-blue-500/10 border border-blue-500/30 rounded-lg">
              <p className="text-sm text-blue-300 mb-4">
                <strong>Getting Started:</strong> To run the Analysis Studio locally, follow these steps:
              </p>
              <code className="text-xs bg-slate-900 p-3 rounded block text-slate-300 overflow-x-auto">
                {`# Install dependencies
pip install -r streamlit_requirements.txt

# Run the Streamlit app
streamlit run streamlit_app.py

# Open your browser to http://localhost:8501`}
              </code>
            </div>

            <div className="flex gap-3 mt-8">
              <button
                onClick={() => setShowStreamlitInfo(false)}
                className="flex-1 px-4 py-3 bg-slate-700 hover:bg-slate-600 rounded-lg font-semibold transition"
              >
                Close
              </button>
              <button className="flex-1 px-4 py-3 bg-blue-600 hover:bg-blue-700 rounded-lg font-semibold transition flex items-center justify-center gap-2">
                <GitBranch size={18} />
                View Repository
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Footer */}
      <footer className="py-12 px-4 bg-slate-900/50 border-t border-slate-700">
        <div className="max-w-6xl mx-auto">
          <div className="grid md:grid-cols-4 gap-8 mb-8">
            <div>
              <h3 className="font-bold text-blue-400 mb-4">Project</h3>
              <ul className="space-y-2 text-slate-400 text-sm">
                <li><a href="#" className="hover:text-blue-400 transition">Features</a></li>
                <li><a href="#" className="hover:text-blue-400 transition">Documentation</a></li>
                <li><a href="#" className="hover:text-blue-400 transition">GitHub</a></li>
              </ul>
            </div>
            <div>
              <h3 className="font-bold text-blue-400 mb-4">Resources</h3>
              <ul className="space-y-2 text-slate-400 text-sm">
                <li><a href="#" className="hover:text-blue-400 transition">Quick Start</a></li>
                <li><a href="#" className="hover:text-blue-400 transition">API Reference</a></li>
                <li><a href="#" className="hover:text-blue-400 transition">Examples</a></li>
              </ul>
            </div>
            <div>
              <h3 className="font-bold text-blue-400 mb-4">Community</h3>
              <ul className="space-y-2 text-slate-400 text-sm">
                <li><a href="#" className="hover:text-blue-400 transition">Contribute</a></li>
                <li><a href="#" className="hover:text-blue-400 transition">Issues</a></li>
                <li><a href="#" className="hover:text-blue-400 transition">Discussions</a></li>
              </ul>
            </div>
            <div>
              <h3 className="font-bold text-blue-400 mb-4">About</h3>
              <ul className="space-y-2 text-slate-400 text-sm">
                <li><a href="#" className="hover:text-blue-400 transition">MIT License</a></li>
                <li><a href="#" className="hover:text-blue-400 transition">Privacy</a></li>
                <li><a href="#" className="hover:text-blue-400 transition">Contact</a></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-slate-700 pt-8 text-center text-slate-400 text-sm">
            <p>AI Future Directions — Pioneering Tomorrow's AI Innovations</p>
            <p className="mt-2">© 2025 Edge AI Innovations. MIT Licensed.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
