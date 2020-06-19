import cv2
import numpy as np
import random

img = cv2.imread('dog.jpg')
print(img.shape) #720, 960, 3
x,y,z = img.shape
print(x)
