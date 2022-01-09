
    
import cv2
import cvzone

from cvzone.FaceMeshModule import FaceMeshDetector
cap = cv2.VideoCapture('mixkit-green-eye-blinking-4257.mp4')
detector = FaceMeshDetector(maxFaces=1)

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES)== cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    success, img = cap.read()
    # img, faces= detector.findFaceMesh(img)
    img = cv2.resize(img, (630, 360))
    cv2.imshow("kamal", img
    cv2.waitKey(3);)
