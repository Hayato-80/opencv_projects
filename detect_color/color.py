import cv2 as cv
import numpy as np

import math

def clahe(frame):
    # make clahe and histogram equalization
    yuv_image = cv.cvtColor(frame, cv.COLOR_BGR2YUV)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    yuv_image[:, :, 0] = clahe.apply(yuv_image[:, :, 0])
    frame = cv.cvtColor(yuv_image, cv.COLOR_YUV2BGR)
    return frame

def color(frame):
    
    frame = clahe(frame)
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    low_1 = np.array([0, 50, 50])
    high_1 = np.array([5, 255, 255])
    low_2 = np.array([175, 50, 50])
    high_2 = np.array([180, 255, 255])

    mask_1 = cv.inRange(frame_hsv,low_1,high_1)
    mask_2 = cv.inRange(frame_hsv,low_2,high_2)
    mask = mask_1 + mask_2
    res = cv.bitwise_and(frame, frame, mask=mask)
    return mask, res

def label(mask, out):
    labels, label_img, stats, centroids = cv.connectedComponentsWithStats(mask)
    labels = labels - 1
    stats = np.delete(stats,0,0)
    centroids = np.delete(centroids,0,0)

    if labels >= 1:
        max_idx = np.argmax(stats[:,4])

        x = stats[max_idx][0]
        y = stats[max_idx][1]
        w = stats[max_idx][2]
        h = stats[max_idx][3]
        s = stats[max_idx][4]

        mx = int(centroids[max_idx][0])
        my = int(centroids[max_idx][1])
        cv.putText(out, "CoM: (X: %d, Y: %d)"%(mx, my), (x-15, y+h+15), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 0))
        cv.putText(out, "Area: %d"%(s), (x, y+h+30), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 0))
        out = cv.rectangle(out,(x,y),(x+w, y+h), (0, 255, 0))
        return out


if __name__ == '__main__':

    cap = cv.VideoCapture(0,700)
    if not cap.isOpened():
        print("Error: Could not open camera.")

    while True:
        _, frame = cap.read()
        cv.imshow('Video', frame)
        frame = cv.medianBlur(frame, 5)

        mask, out = color(frame)

        out = label(mask, out)
        cv.imshow('mask final',out)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()