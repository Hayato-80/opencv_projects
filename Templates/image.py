import sys
import numpy as np

import cv2 as cv

def image():
    img = cv.imread("your image path")

    cv.imshow("image", img)
    cv.waitKey(0)

if __name__ == "__main__":
    image()