import cv2
import numpy as np

img = cv2.imread('pic.jpg')
points=[]
def warper(pts):
    p = np.array([pts[0],pts[1],pts[2],pts[3]],np.float32)
    q = np.array([(0,0),(1000,0),(0,1000),(1000,1000)],np.float32)
    perspective = cv2.getPerspectiveTransform(p,q)
    transformed = cv2.warpPerspective(img,perspective,(1000,1000))
    cv2.imshow("Img",img)
    cv2.imshow("Img1",transformed)

def mouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        if len(points)==4:
            warper(points)

while True:
    cv2.imshow("Img",img)
    cv2.namedWindow("Img")
    cv2.setMouseCallback("Img",mouse)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()