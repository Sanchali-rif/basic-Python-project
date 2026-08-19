# AI Image Classifier

An intelligent image classification application built with **Streamlit** and **TensorFlow/Keras**. Upload an image and let AI identify what's in it with top-3 predictions!

## Features

✨ **Key Capabilities:**
- 🖼️ Upload and classify images (JPG, PNG formats)
- 🤖 Pre-trained MobileNetV2 model from ImageNet
- 📊 Top-3 predictions with confidence scores
- ⚡ Fast inference using optimized mobile neural network
- 🎨 Clean, user-friendly Streamlit interface
- 💾 Model caching for optimal performance

## Tech Stack

- **Framework:** Streamlit
- **Deep Learning:** TensorFlow/Keras
- **Computer Vision:** OpenCV, NumPy
- **Image Processing:** Pillow (PIL)
- **Model:** MobileNetV2 (pre-trained on ImageNet)
- **Python:** >=3.14

## Installation

1. **Clone/Navigate to the project:**
```bash
cd project_3
```

2. **Install the package and dependencies:**
```bash
python -m pip install -e .
```

This will install:
- Streamlit
- TensorFlow/Keras
- OpenCV (cv2)
- NumPy
- Pillow

## Usage

### Run the Application

```bash
streamlit run src/project_3/__init__.py
```

The app will open in your browser (typically at `http://localhost:8501`).

### How to Use

1. Click "Choose an image..." to upload an image file (JPG or PNG)
2. The uploaded image will be displayed
3. AI will automatically classify the image
4. View the top-3 predictions with confidence scores

## Project Structure

```
project_3/
├── README.md                 # This file
├── pyproject.toml            # Project configuration
└── src/
    └── project_3/
        └── __init__.py       # Main Streamlit app
```

## How It Works

1. **Image Upload:** User uploads an image via Streamlit file uploader
2. **Preprocessing:** Image is resized to 224×224 and normalized for MobileNetV2
3. **Classification:** MobileNetV2 model predicts image class from ImageNet categories
4. **Results:** Top-3 predictions with confidence percentages are displayed

## Model Details

- **Model:** MobileNetV2
- **Pre-trained on:** ImageNet dataset
- **Input Size:** 224×224 pixels
- **Output:** Classification confidence scores for 1000 ImageNet classes

## Requirements

- Python >=3.14
- 500+ MB disk space (for model download on first run)
- Modern web browser for Streamlit UI

## Troubleshooting

**Issue:** Model download is slow on first run
- **Solution:** The model (~100MB) downloads once and is cached locally. Subsequent runs are instant.

**Issue:** "Error classifying image"
- **Solution:** Ensure the image is in JPG or PNG format and is a valid image file.

**Issue:** "CUDA out of memory" (if using GPU)
- **Solution:** The model runs on CPU by default. TensorFlow will automatically use available GPU if present.

## Future Enhancements

- 📸 Batch image processing
- 🎨 Custom model support
- 🔍 Real-time webcam classification
- 📈 Confidence score visualization
- 🌍 Support for multiple pre-trained models

---

**Part of the AI Agent Workspace** - A monorepo of AI/ML projects built with Python, LangChain, and modern AI frameworks.
