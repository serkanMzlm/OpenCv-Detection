import cv2

def HVS_Detect(mouse, x, y, flags, param):
    if mouse == cv2.EVENT_LBUTTONDOWN: 
        h = hsv[y, x, 0]
        s = hsv[y, x, 1]
        v = hsv[y, x, 2]

        hsvUzayi = 'HSV: ' + str(h) + ' ' + str(s) + ' ' + str(v)
        print(hsvUzayi)
        cv2.imshow("img", img)
cap = cv2.VideoCapture(0)

while True:

    _, img = cap.read() 
    img = cv2.resize(img,(640,480)) 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
    cv2.imshow("img", img)
    cv2.setMouseCallback('img',HVS_Detect) 
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
