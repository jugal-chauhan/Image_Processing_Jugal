import cv2

img = cv2.imread('backg.jpg')
print(img.shape)
x = int(input('enter lenght'))
y = int(input('enter breadth'))

cv2.line(img,(0,0),(x,y),(255,255,0),4)
cv2.imshow('window',img)
cv2.waitKey(0)