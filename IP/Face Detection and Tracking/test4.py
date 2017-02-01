import cv2
import dlib
import numpy as np

model = "shape_predictor_68_face_landmarks.dat"
landmarks_obj = dlib.shape_predictor(model)
faces = dlib.get_frontal_face_detector()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rect = faces(frame)

    for i , d in enumerate(rect, 1):
        cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0,255,0), 2)
        detected_landmarks = landmarks_obj(frame, d).parts()
        landmarks = np.matrix(([[p.x, p.y] for p in detected_landmarks]))
        for idx, point in enumerate(landmarks):
            pos= (point[0,0], point[0,1])
            cv2.circle(frame, pos, 1, (100,10,50), 1)

    cv2.imshow("frame ", frame)

    if cv2.waitKey(10) & 0xff== 27: #press escape to exit
        break

cap.release()
cv2.destroyAllWindows()