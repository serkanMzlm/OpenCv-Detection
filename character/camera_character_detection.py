import cv2
import pytesseract
from time import time

cap = cv2.VideoCapture(0)

ctime = ptime = 0
while True:
    _,img = cap.read()
    img = cv2.flip(img,1)
    img = cv2.resize(img, (640, 480)) 
    hImg, wImg,_ = img.shape 

    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines(): 
        b = b.split(' ')
        x, y = int(b[1]), int(b[2])
        w, h = int(b[3]), int(b[4])
        cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)

    ctime = time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(img, str(int(fps)), (75, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20,230,20), 2)
    cv2.imshow("Result",img)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()