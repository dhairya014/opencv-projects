import cv2
import mediapipe as mp
import math
import numpy as np
import screen_brightness_control as sbc
import time


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    model_complexity=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)


cap = cv2.VideoCapture(0)


# Camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# Minimum and maximum finger distance
MIN_DISTANCE = 0.08
MAX_DISTANCE = 0.30

# Brightness range
MIN_BRIGHTNESS = 10
MAX_BRIGHTNESS = 90

# Smoothing factor
# Smaller = smoother but slower
# Larger = faster but less smooth
SMOOTHING = 0.15

# Minimum brightness change before updating Windows
CHANGE_THRESHOLD = 2

# Store previous values
smooth_brightness = 50
last_brightness = -1

# Control how often Windows brightness is updated
last_update_time = 0
UPDATE_INTERVAL = 0.08


while True:

    success, frame = cap.read()

    if not success:
        print("Could not read camera.")
        break


    # Mirror the camera
    frame = cv2.flip(frame, 1)

    # Frame dimensions
    h, w, _ = frame.shape

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    results = hands.process(rgb_frame)



    if results.multi_hand_landmarks:

        hand_landmarks = results.multi_hand_landmarks[0]


        mp_draw.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS
        )


        # MediaPipe landmarks:
        # Thumb tip = 4
        # Index tip = 8

        thumb = hand_landmarks.landmark[4]
        index = hand_landmarks.landmark[8]


        # MediaPipe coordinates are normalized:
        #
        # x = 0 → left
        # x = 1 → right
        #
        # y = 0 → top
        # y = 1 → bottom

        thumb_x = thumb.x
        thumb_y = thumb.y

        index_x = index.x
        index_y = index.y


        length = math.hypot(
            index_x - thumb_x,
            index_y - thumb_y
        )


        brightness = np.interp(
            length,
            [MIN_DISTANCE, MAX_DISTANCE],
            [MIN_BRIGHTNESS, MAX_BRIGHTNESS]
        )


        # Convert to integer
        brightness = int(brightness)


        # Keep brightness within limits
        brightness = max(
            MIN_BRIGHTNESS,
            min(MAX_BRIGHTNESS, brightness)
        )


        smooth_brightness = (
            SMOOTHING * brightness
            +
            (1 - SMOOTHING) * smooth_brightness
        )

        smooth_brightness = int(
            smooth_brightness
        )


        current_time = time.time()

        if (
            current_time - last_update_time
            >= UPDATE_INTERVAL
        ):

            if (
                last_brightness == -1
                or abs(
                    smooth_brightness
                    - last_brightness
                ) >= CHANGE_THRESHOLD
            ):

                try:

                    sbc.set_brightness(
                        smooth_brightness
                    )

                    last_brightness = (
                        smooth_brightness
                    )

                except Exception as e:

                    print(
                        "Brightness error:",
                        e
                    )

            last_update_time = current_time


        thumb_px = int(thumb_x * w)
        thumb_py = int(thumb_y * h)

        index_px = int(index_x * w)
        index_py = int(index_y * h)


        cv2.circle(
            frame,
            (thumb_px, thumb_py),
            10,
            (255, 0, 0),
            -1
        )

        cv2.circle(
            frame,
            (index_px, index_py),
            10,
            (255, 0, 0),
            -1
        )


        cv2.line(
            frame,
            (thumb_px, thumb_py),
            (index_px, index_py),
            (255, 0, 0),
            3
        )


        cv2.putText(
            frame,
            f"Distance: {length:.3f}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Brightness: {smooth_brightness}%",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )


        bar_x = 20
        bar_y = 120

        bar_width = 300
        bar_height = 25

        # Background
        cv2.rectangle(
            frame,
            (bar_x, bar_y),
            (
                bar_x + bar_width,
                bar_y + bar_height
            ),
            (50, 50, 50),
            -1
        )


        # Filled portion
        fill_width = int(
            bar_width
            * smooth_brightness
            / 100
        )

        cv2.rectangle(
            frame,
            (bar_x, bar_y),
            (
                bar_x + fill_width,
                bar_y + bar_height
            ),
            (0, 255, 0),
            -1
        )


        # Border
        cv2.rectangle(
            frame,
            (bar_x, bar_y),
            (
                bar_x + bar_width,
                bar_y + bar_height
            ),
            (255, 255, 255),
            2
        )


    else:

        cv2.putText(
            frame,
            "No hand detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )


    cv2.imshow(
        "Hand Brightness Control",
        frame
    )


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()

cv2.destroyAllWindows()

hands.close()

