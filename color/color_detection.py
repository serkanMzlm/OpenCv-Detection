#!/usr/bin/python3

import cv2
import numpy as np

cap = cv2.VideoCapture(0) 
while True:
    _,img = cap.read() 
    flipImg = cv2.flip(img,1) 
    hsvImg = cv2.cvtColor(flipImg,cv2.COLOR_BGR2HSV)

    #HSV Upper and Lower Bounds for Colors
    # Orange
    lowerOrange = np.array([0, 100, 100])
    upperOrange = np.array([22, 255, 255])
    # Yellow
    lowerYellow = np.array([22, 146, 190])
    upperYellow = np.array([38, 180, 250])
    # Green
    lowerGreen = np.array([38, 100, 100])
    upperGreen = np.array([75, 255, 255])
    # Blue
    lowerBlue = np.array([75, 100, 100])
    upperBlue = np.array([130, 255, 255])
    # Purple
    lowerPurple = np.array([130, 100, 100])
    upperPurple = np.array([160, 255, 255])
    # Red
    lowerRed = np.array([160, 100, 100])
    upperRed = np.array([179, 255, 255])


    blueMask = cv2.inRange(hsvImg, lowerBlue, upperBlue)
    blue = cv2.bitwise_and(flipImg, flipImg, mask=blueMask)

    cv2.imshow("img",flipImg)
    cv2.imshow("blueMask",blueMask)
    cv2.imshow("blue",blue)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release() 
cv2.destroyAllWindows()