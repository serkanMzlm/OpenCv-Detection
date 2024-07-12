#!/usr/bin/python3

import cv2
import os
import numpy as np

current_path = os.getcwd()
parent_path = os.path.abspath(os.path.join(current_path, ".."))
images_path = os.path.abspath(os.path.join(parent_path, "images"))

def HVS_Detect(mouse, x, y, flags, param):
    if mouse == cv2.EVENT_LBUTTONDOWN: #mouse left
        h = hsv[y, x, 0]
        s = hsv[y, x, 1]
        v = hsv[y, x, 2]

        hsvUzayi = 'HSV: ' + str(h) + ' ' + str(s) + ' ' + str(v)
        cv2.putText(img, "+", (x-14, y+12), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)
        cv2.putText(img, hsvUzayi, (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255),2 )
        cv2.imshow("img", img)

img = cv2.imread(images_path + '/color.jpg') 
img = cv2.resize(img,(640,480)) 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
cv2.imshow("img", img)
cv2.setMouseCallback('img',HVS_Detect) 
cv2.waitKey(0)
cv2.destroyAllWindows()