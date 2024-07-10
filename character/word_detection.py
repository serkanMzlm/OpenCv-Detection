#!/usr/bin/python3

import cv2 
import pytesseract as pt


img = cv2.imread("../images/character_1.png")
img = cv2.resize(img,[640,480])
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hImg, wImg, _ = img.shape 

boxes = pt.image_to_data(img) 
for x,b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        if len(b) == 12: 
            x,y = int(b[6]),int(b[7])
            w,h = int(b[8]),int(b[9])
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2) 
            cv2.putText(img, b[11], (x,y), cv2.FONT_HERSHEY_COMPLEX,1, (0,0,255), 2)
    cv2.imshow("",img)
cv2.waitKey(0)