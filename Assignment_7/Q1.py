import cv2
import numpy as np 

def nothing(x):
    pass

cam = cv2.VideoCapture(0)

cv2.namedWindow('cam')
cv2.createTrackbar('High_Hue','cam',0,180,nothing)
cv2.createTrackbar('Low_Hue','cam',0,180,nothing)
cv2.createTrackbar('High_Saturation','cam',0,255,nothing)
cv2.createTrackbar('low_Saturation','cam',0,255,nothing)
cv2.createTrackbar('High_Value','cam',0,255,nothing)
cv2.createTrackbar('Low_Value','cam',0,255,nothing)


while True:
    x,display = cam.read()
    hsv = cv2.cvtColor(display, cv2.COLOR_BGR2HSV)

    High_Hue = cv2.getTrackbarPos('High_Hue','cam')
    Low_Hue = cv2.getTrackbarPos('Low_Hue','cam')
    High_Saturation = cv2.getTrackbarPos('High_Saturation','cam')
    Low_Saturation = cv2.getTrackbarPos('Low_Saturation','cam')
    High_Value= cv2.getTrackbarPos('High_Value','cam')
    Low_Value= cv2.getTrackbarPos('Low_Value','cam')

    Low_hsv = np.array([Low_Hue,Low_Saturation,Low_Value])
    High_hsv = np.array([High_Hue,High_Saturation,High_Value])

    mask= cv2.inRange(hsv,Low_hsv,High_hsv)
    result = cv2.bitwise_and(display,display,mask=mask)

    cv2.imshow('display',display)
   
    cv2.imshow('cam',result)

    if cv2.waitKey(1) & 0xFF==27:
        break