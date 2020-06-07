import cv2
import time
import math

cap = cv2.VideoCapture(0)
count = 0

while True :
    count = count + 1
    StartTime = time.time()

    for i in range(0, 5):
        print(i)
        time.sleep(1)
    
    EndTime = time.time()
    RemTime = EndTime - StartTime
    print("RemTime = %s" % RemTime)

    x , frame = cap.read()
    flipped = cv2.flip(frame,-1)
    
    if cv2.waitKey(5) & 0xFF == ord('q') :
        break
    if math.floor(RemTime) % count == 0 :
        cv2.imshow('Image',flipped)
    else :
        cv2.imshow('Image', frame)
