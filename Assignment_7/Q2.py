import cv2
import numpy as np


img = cv2.imread('dog.jpg')
width = int(img.shape[1] / 10)
height = int(img.shape[0] / 10)
dim = (width, height)
#resize the original image
size_change = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('Original',size_change)

img_gray = cv2.cvtColor(size_change, cv2.COLOR_BGR2GRAY)
img_gray_smooth = cv2.GaussianBlur(img_gray,(5,5),0)
ret,img_gray_smooth_thresh = cv2.threshold(img_gray_smooth,180,255,cv2.THRESH_BINARY)
canny = cv2.Canny(img_gray_smooth_thresh,300, 300)

cv2.imshow('Canny', canny)

contour, heirarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
areas = [cv2.contourArea(c) for c in contour]
max_index = np.argmax(areas)
max_contour = contour[max_index]
perimeter = cv2.arcLength(max_contour, True)
coordinates = cv2.approxPolyDP(max_contour, 0.01*perimeter, True)
cv2.drawContours(size_change, [coordinates], -1, (0,0,255), 1)

pt1 = np.array([coordinates[1], coordinates[0], coordinates[2], coordinates[3]], np.float32)
pt2 = np.array([(0,0), (500,0), (0,600), (500,600)], np.float32)

pers = cv2.getPerspectiveTransform(pt1, pt2)
new = cv2.warpPerspective(size_change, pers, (500,600))

cv2.imshow('new', new)
cv2.waitKey(0)