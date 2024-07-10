import cv2
import numpy as np

def HVS_Detect(mouse, x, y, flags, param):

    if mouse == cv2.EVENT_LBUTTONDOWN: 
        h = hsvImg[y, x, 0]
        s = hsvImg[y, x, 1]
        v = hsvImg[y, x, 2]
        print("HSV:",h,s,v)
        lower = np.array([h - 8, s - 25, v - 50])
        upper = np.array([h + 8, s + 25,v+50])
        Mask = cv2.inRange(hsvImg, lower, upper) 
        color = cv2.bitwise_and(flipImg, flipImg, mask=Mask) 
        cv2.imshow("greenMask", Mask)
        cv2.imshow("green", color)

cap = cv2.VideoCapture(0) 

while True:
    _,img = cap.read() 
    flipImg = cv2.flip(img,1) 
    hsvImg = cv2.cvtColor(flipImg,cv2.COLOR_BGR2HSV) 
    cv2.imshow("img", flipImg)
    cv2.setMouseCallback('img', HVS_Detect)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release() 
cv2.destroyAllWindows() 
