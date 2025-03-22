import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

img = cv.imread('./Lenna.png')
template = cv.imread('./Lenna_template.png')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

match = cv.matchTemplate(img_gray,template_gray, cv.TM_CCOEFF_NORMED)

# Check the where the value is maximum
# plt.imshow(match, cmap='gray')
# plt.show()

# Find the location of the maximum value
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(match)

# Drawing bbox
top_left = max_loc
temp_h,temp_w,  = template.shape[:2]
bottom_right = (top_left[0]+temp_w, top_left[1]+temp_h)

# Result
result = cv.rectangle(img, top_left, bottom_right, (0,255,0),2)

cv.imshow('result',result)
cv.waitKey(0)
cv.destroyAllWindows()