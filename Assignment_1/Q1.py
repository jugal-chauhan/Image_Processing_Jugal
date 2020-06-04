import cv2

cap=cv2.VideoCapture(0)
i = 0
n = 5
while True:
    x, frame = cap.read()
    flipped = cv2.flip(frame,-1)
     
    if i<n:
        cv2.imshow('Image',frame)
        i+=1
    
    else:
        cv2.imshow('Image',flipped)

    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break