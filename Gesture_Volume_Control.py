import cv2 as cv
import time
import math
import subprocess
import numpy as np
import HandTrackingFunctionalP as htm

detector = htm.HandDetector()

capture = cv.VideoCapture(0)

curr_time = 0
prev_time = 0
last_volume = None
volBar = 400
volPerc = 0

def set_volume(level):
    level = int(level * 100)
    script = f"set volume output volume {level}"
    subprocess.run(["osascript", "-e", script])

while True:
    isTrue, frame = capture.read()
    img = detector.showPoints(frame)
    lm_list = detector.returnPoints(frame)

    if len(lm_list) != 0:
        x1, y1 = (lm_list[4][1], lm_list[4][2])
        x2, y2 = (lm_list[8][1], lm_list[8][2])
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv.circle(frame, (x1, y1), 15, (0, 255, 255), -1)
        cv.circle(frame, (x2, y2), 15, (0, 255, 255), -1)
        cv.circle(frame, (cx, cy), 15, (0, 255, 255), -1)
        cv.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 4)

        length = math.hypot(x2 - x1, y2 - y1)

        volume = np.interp(length, [50, 300], [0.0, 1.0])
        volume = max(0.0, min(1.0, volume))

        # Only change volume if the difference from the last volume is significant
        if last_volume is None or abs(volume - last_volume) > 0.01:
            set_volume(volume)
            last_volume = volume  # Update the last known volume

        volBar = np.interp(length, [50, 300], [400, 150])
        volPerc = np.interp(length, [50, 300], [0, 100])

        if length < 50:
            cv.circle(frame, (cx, cy), 15, (0, 255, 0), -1)

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    f = cv.flip(frame, 1)


    cv.rectangle(f, (50, 150), (85, 400), (0, 255, 0), 3)
    cv.rectangle(f, (50, int(volBar)), (85, 400), (0, 255, 0), cv.FILLED)
    cv.putText(f, f"Volume: {int(volPerc)}%", (40, 450), cv.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 0), 2)
    cv.putText(f, f"FPS: {int(fps)}", (20, 100), cv.FONT_HERSHEY_TRIPLEX, 3, (255, 0, 0), 2)
    cv.imshow('Hand Tracking', f)


    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
