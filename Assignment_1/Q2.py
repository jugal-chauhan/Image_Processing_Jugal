import cv2

cap= cv2.VideoCapture(0)
counter = 0

while True:
    x,frame= cap.read()
    horiflip = cv2.flip(frame,1)
    counter+=1

    if counter%2 == 0:
        cv2.imshow('HoriImage',frame)

    else:
        cv2.imshow('HoriImage',horiflip)

    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break