import cv2
import numpy as np
import time
import random

img = cv2.imread('dog.jpg')
x,y,z = img.shape
print(y)

x1 = 0
y1 = 0
xd = int(x/7)
yd = int(y/7)
x2 = xd
