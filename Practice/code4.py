#flipping frame after a particular interval - vertically and horizontally both

import cv2

cap= cv2.VideoCapture(0)
frameno = 0
n = int(input("Enter value : "))
n = n + 1

def flipfunc(frameno):
    if frameno % n == 0:
        cv2.imshow('frame', flipVertical)
        print(frameno)
    else:
        cv2.imshow('frame', frame)

while True:
    ret, frame = cap.read()
    flipVertical = cv2.flip(frame, -1) #to flip horizontally change -1 to 1
    frameno = frameno + 1

    flipfunc(frameno)

    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break

cap.release()