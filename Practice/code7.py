# display equal square boxes of random color over written on an image

import cv2
import numpy as np
import random

img = cv2.imread('dog.jpg')
print(img.shape) #720, 960, 3
x,y,z = img.shape
print(x)
print(y)
print(z)
x1 = 0
y1 = 0
xd = int(x/7)
yd = int(y/7)
x2 = xd
y2 = yd


while True:
    while x2 <= x:
        while y2 <= y:
            cv2.imshow('frame',img)
            rand = np.random.randint(0,255,(3))
            img[x1:x2, y1:y2] = rand

            y1 += yd
            y2 += yd
        y1 = 0
        y2 = yd
        x1 += xd
        x2 += xd
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

cv2.imshow('frame', img)
cv2.waitKey(0)