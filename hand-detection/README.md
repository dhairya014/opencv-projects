# Hand Detection Using Python and OpenCV

A real-time hand detection project using Python, OpenCV, and MediaPipe. It detects hands through a webcam and displays hand landmarks and their connections on the video feed.

## Demo

![Hand Detection Demo](assets/hand_detection_demo.gif)

## Features

- Real-time hand detection using a webcam
- Supports detection of up to two hands
- Displays hand landmarks and connections
- Mirrors the webcam feed for a natural viewing experience
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

Run the following command from the `hand-detection` folder:

```bash
python hand_detection.py
```

The webcam window will open and display detected hand landmarks. Press `q` to close the window.

## Project Structure

```text
hand-detection/
├── assets/
│   └── hand_detection_demo.gif
├── hand_detection.py
├── requirements.txt
└── README.md
```

## Notes

- Allow webcam access if your operating system requests permission.
- Close other applications that may be using the webcam if it cannot be opened.
- Library compatibility can depend on your installed Python version.

---

Part of the [OpenCV Projects](../README.md) portfolio.
