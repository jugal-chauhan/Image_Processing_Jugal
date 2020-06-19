# use numpy array, zip function and random in Image Processing

import cv2
import random 
import numpy as np

zero = np.zeros((400,400), np.uint8)
one = 255*(np.ones((400,400), np.uint8))

random = np.random.randint(0,255, (500,500,3), np.uint8)

# cv2.imshow('frame', random)
# cv2.waitKey(0)

list_1 = (1,2,3)
list_2 = (4,5,6)
zipped = zip(list_1, list_2)
print(zipped)

list_combined = [(1,2), (2,3), (3,4)]

for x, y, z in zip(*list_combined):
    print(x)
    print(y)
    print(z)