# ✋ Screen Brightness Control Using Hand Gestures

Control your computer's screen brightness using hand gestures with Python, OpenCV, and MediaPipe.

## 🎥 Demo

[Watch the demo video](assets/demo.mp4)

## ✨ Features

- Real-time hand tracking using MediaPipe
- Brightness control using the distance between thumb and index finger
- Smooth brightness adjustment
- Live display of hand landmarks and brightness percentage
- Press `q` to quit the application

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- screen-brightness-control

## 📁 Project Structure

```text
screen-brightness-control/
├── assets/
│   └── demo.mp4
├── brightness_control.py
├── requirements.txt
└── README.md
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/dhairya014/opencv-projects.git
cd opencv-projects
```

Install dependencies:

```bash
pip install -r screen-brightness-control/requirements.txt
```

Run the program:

```bash
python screen-brightness-control/brightness_control.py
```

## ⚙️ How It Works

1. The webcam detects your hand.
2. MediaPipe tracks your thumb tip and index fingertip.
3. Their distance is mapped to a brightness level.
4. The program adjusts the screen brightness.

## ⚠️ Requirements

- Python
- A working webcam
- A compatible display supported by `screen-brightness-control`

Note: Brightness adjustment may not work on every external monitor.

## 👨‍💻 Author

**Dhairya**

GitHub: [@dhairya014](https://github.com/dhairya014)