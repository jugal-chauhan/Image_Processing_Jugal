import cv2
import numpy as np 
import random

img = cv2.imread('car.jpeg')
print(img.shape)
p = 0
q = 0

#300 168 3
x = int(300/7)
y = int(168/7)

while True:
    x1 = 0
    
    while True:
        cv2.rectangle(img,(p,q),(x,y),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
        p += q
        x += y

        if x > 640:
            break
    q += x
    y += x
    if y > 300:
        break

cv2.imshow('Frame', img)
cv2.waitKey(0)