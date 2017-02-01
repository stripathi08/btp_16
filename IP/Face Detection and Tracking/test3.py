import cv2
import dlib

model = "shape_predictor_68_face_landmarks.dat"
landmarks_obj = dlib.shape_predictor(model)
faces = dlib.get_frontal_face_detector()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    rect = faces(frame)

    for i , d in enumerate(rect, 1):
        cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0,255,0), 2)
        landmarks = landmarks_obj(frame, d)
        pnt = landmarks.part(48)
        pnt2 = landmarks.part(54)
        nose = landmarks.part(30)
        cv2.rectangle(frame,(pnt.x, pnt.y), (pnt2.x, pnt2.y), (255, 0, 0))
        cv2.circle(frame, (nose.x, nose.y), 5, (0,255,0), 1)

    cv2.imshow("frame ", frame)

    if cv2.waitKey(10) & 0xff== 27:
        break

cap.release()
cv2.destroyAllWindows()