import cv2 as cv
import numpy as np

import math

def color(frame):
    # hsv_image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # hsv_image[:, :, 2] = cv.equalizeHist(hsv_image[:, :, 2])
    # image_corrected = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)

    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    low = np.array([0, 100, 50])
    high = np.array([10, 255, 255])

    mask = cv.inRange(frame_hsv,low,high)

    res = cv.bitwise_and(frame, frame, mask=mask)
    return res

if __name__ == '__main__':

    cap = cv.VideoCapture(0,700)
    if not cap.isOpened():
        print("Error: Could not open camera.")

    # cap.set(cv.CAP_PROP_FRAME_WIDTH, 1024)
    # cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
    while True:
        _, frame = cap.read()
        cv.imshow('Video', frame)

        mask = color(frame)
        cv.imshow('mask',mask)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()