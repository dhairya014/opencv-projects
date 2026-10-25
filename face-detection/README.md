# Face Detection Using Python and OpenCV

A real-time face detection project using Python, OpenCV, and MediaPipe. It uses a webcam to detect faces and draw detection annotations around them.

## Demo

![Face Detection Demo](assets/face_detection_demo.gif)

## Features

- Real-time face detection using a webcam
- Draws visual annotations for detected faces
- Mirrors the webcam feed for a natural viewing experience
- Uses MediaPipe's face detection solution
- Press `q` to exit the application

## Technologies Used

- Python
- OpenCV
- MediaPipe

## Requirements

- Python installed on your computer
- A working webcam
- The libraries listed in `requirements.txt`

## Installation

1. Open a terminal in this project folder.
2. (Optional) Create and activate a virtual environment.
3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

Run the following command from the `face-detection` folder:

```bash
python face_detection.py
```

The webcam window will open and show face detection results. Press `q` to close the window.

## Project Structure

```text
face-detection/
├── assets/
│   └── face_detection_demo.gif
├── face_detection.py
├── requirements.txt
└── README.md
```

## Notes

- Allow webcam access if your operating system requests permission.
- Close other applications that may be using the webcam if it cannot be opened.
- Library compatibility can depend on your installed Python version.

---

Part of the [OpenCV Projects](../README.md) portfolio.
