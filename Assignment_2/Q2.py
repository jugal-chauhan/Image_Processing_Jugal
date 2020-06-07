import cv2

cap = cv2.VideoCapture(0)
count = 0

while True:
    x,frame = cap.read()
    cv2.imshow('image',frame)


    dataset_img_name = "dataset_img{}.jpg".format(count)
    cv2.imwrite(dataset_img_name, frame)
    count += 1

    if cv2.waitKey(1) & 0xff == ord('q'):
        break