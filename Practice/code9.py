import cv2
import numpy as np
import random

# template = cv2.imread('template.png')
# temp_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
# w = template.shape[1]
# h = template.shape[0]

# img = cv2.imread('test.png')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# res = cv2.matchTemplate(img_gray, temp_gray, cv2.TM_CCOEFF)

# loc = np.where(res>=0.7)
# for x,y in zip(*loc[::-1]):
#     cv2.rectangle(img, (x,y), (x+w, y+h), (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 1)

# cv2.imshow('frame', img)
# cv2.waitKey(0)

img1 = cv2.imread('a.png')
img2 = cv2.imread('b.png')

var = cv2.bitwise_not(img1)
var2 = cv2.bitwise_xor(img2)

cv2.imshow('frame', var2)
cv2.waitKey(0)