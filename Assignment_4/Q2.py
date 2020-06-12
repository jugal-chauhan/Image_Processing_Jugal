import cv2
import numpy as np
img=cv2.imread('car.jpeg')

p = False
q = False

def crop_func(event,x,y,flags,param):
    global pts,p,q

    if event == cv2.EVENT_LBUTTONDOWN:
        if p == False:
            pts = [(x,y)]
            p = True
        elif q == False:
            pts.append((x,y))
            q = True
        if len(pts) == 2:
            ty, by, tx, bx = pts[0][1],pts[1][1],pts[0][0],pts[1][0]
            crop = img[ty:by, tx:bx]
            cv2.imshow('Frame',crop)
            
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',crop_func)
cv2.imshow('Frame',img)