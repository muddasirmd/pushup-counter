🐍 1. Create Virtual Environment
- python -m venv venv
- source venv/bin/activate      # Linux/macOS
- venv\Scripts\activate       # Windows

📦 2. Install Dependencies
- pip install opencv-python mediapipe numpy
- pip freeze > requirements.txt
OR
- pip install -r requirements.txt

🧪 3. Add Sample Video
- cp /path/to/your/video.mp4 data/pushups.mp4
- (or just manually place your video inside data/)

🧪 4. Add Sample Video
- cp /path/to/your/video.mp4 data/pushups.mp4
- (or just manually place your video inside data/)

🚀 5. Run Project
- Activate venv: source venv/bin/activate OR venv\Scripts\activate
- python -m src.main


# 💪 Push-up Counter (Python + MediaPipe)

A computer vision project that counts push-ups from a video using pose estimation.

## 🚀 Features
- Detects body joints using MediaPipe
- Calculates arm angle
- Counts push-ups automatically
- Works on video input

## 📦 Installation

```bash
pip install -r requirements.txt