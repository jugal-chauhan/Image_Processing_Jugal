import cv2
import numpy as np
import random
import time

img=cv2.imread('car.jpg')
h,w,c=img.shape
#h=300,w=168
a = 0
b = 0
x = int(300/7)   #x=42
y = int(168/7)   #y=24
row=0
while True: #Y axis loop
    
    if row % 2==0: #Even row
        a1=0
        x=80
        
        while True:
            cv2.rectangle(img,(a,b),(x,y),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
            cv2.imshow('Frame',img)
            cv2.waitKey(500)
            a+=80
            x+=42
            if x>300:
                break

    else: #Odd row
        a=480
        x=300
        
        while True:
            cv2.rectangle(img,(a,b),(x,y),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
            cv2.imshow('Frame',img)
            cv2.waitKey(500)
            a-=80
            x-=42
            if a1<0:
                break

    b+=80
    y+=80
    row+=1
    if y>168:
        break