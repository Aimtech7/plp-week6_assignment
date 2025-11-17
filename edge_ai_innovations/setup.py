from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="edge-ai-innovations",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="TensorFlow Lite Edge AI for recyclable item classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/edge_ai_innovations",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "tensorflow>=2.13.0",
        "numpy>=1.24.0",
        "pillow>=10.0.0",
        "matplotlib>=3.7.0",
    ],
    extras_require={
        "dev": [
            "jupyter>=1.0.0",
            "notebook>=7.0.0",
        ],
        "edge": [
            "tflite-runtime>=2.13.0",
        ],
    },
)
