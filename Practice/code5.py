import cv2

img = cv2.imread('dog.jpg')

cv2.line(img, (0,0), (1000,1000), (0,255,255), 4)
cv2.imshow('frame', img)
cv2.waitKey(0)