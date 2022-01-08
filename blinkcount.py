import cv2
import cvzone

cap = cv2.VideoCapture('mixkit-green-eye-blinking-4257.mp4')

while True:
    success, img = cap.read()
    img=cv2.resize(img, (640,360))
    cv2.imshow("kamal",img)
    cv2.waitKey(1)
    
