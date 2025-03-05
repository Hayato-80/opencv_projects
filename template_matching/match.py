import cv2 as cv
import numpy as np

def match():

if __name__ == '__main__':

    cap = cv.VideoCapture(0,700)
    if not cap.isOpened():
        print("Error: Could not open camera.")

    while True:
        _, frame = cap.read()
        cv.imshow('Video', frame)
        # frame = cv.medianBlur(frame, 5)

        cv.imshow('mask final',frame)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
