#code to draw shaped on an image and their parameter properties

import cv2

img = cv2.imread('dog.jpg')

cv2.line(img, (0,0), (1000,1000), (0,255,255), 4)
cv2.circle(img, (200,200), 20, (255,0,0), -1)
cv2.rectangle(img, (100,100), (200,200), (255,255,0), -1)
cv2.putText(img, 'mozzarella', (100,100), cv2.FONT_HERSHEY_SIMPLEX, 5, (100,100,245), 2)

img[300:700, 400:700] = [0,0,0]

cv2.imwrite('imwrite.jpg', img)
print(img.shape)

cv2.imshow('frame', img)
cv2.waitKey(0)