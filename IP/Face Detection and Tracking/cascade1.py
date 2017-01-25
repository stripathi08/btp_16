import cv2
import numpy as np

#face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye_tree_eyeglasses.xml')  #with glasses
smile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')

hand_cascade = cv2.CascadeClassifier('haarcascades/closed_frontal_palm.xml')  #right hand fist only

cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0),2)

        smiles = smile_cascade.detectMultiScale(roi_gray, 1.9, 18)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx,sy), (sx+sw,sy+sh), (0,255,0),2)

    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in hands:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0,255, 0), 2)

    cv2.imshow('image',image)
    key = cv2.waitKey(30) & 0xff
    if key ==27:
        break
cap.release()
cv2.destroyAllWindows()
