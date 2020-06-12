import cv2
import numpy as np

print("working...")

# img = cv2.imread('car.jpeg', 1)
# img = cv2.line(img, (0,0), (150,150), (255,0,0), 5)
# img = cv2.arrowedLine(img, (0,150), (150,150), (0,255,0), 3)

# cv2.imshow('Image', img)

# #print(img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

array = np.random.randint(0,255,(5,5))
array = array.astype(np.uint8)
cv2.imshow('frame',array)
cv2.waitKey(0)
print(array)


