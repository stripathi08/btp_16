import cv2
import sys
import dlib

predictor_model = "shape_predictor_68_face_landmarks.dat" #pre trained model for face landmark detection
face_detector = dlib.get_frontal_face_detector()
face_pose_predictor = dlib.shape_predictor(predictor_model)

win = dlib.image_window()

ramp_frames = 30
cam = cv2.VideoCapture(0)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 520)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 380)

def get_image():
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray

for i in xrange(ramp_frames): #reject first 30 frames as soon as webcam opens
    temp = get_image()

while True:
    cap_image = get_image()
    detected_faces = face_detector(cap_image)
    #print detected_faces
    #sys.exit()
    win.clear_overlay()
    win.set_image(cap_image)

    for i, face_rect in enumerate(detected_faces, 1):
        # Detected faces are returned as an object with the coordinates
        # of the top, left, right and bottom edges

        #print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(),face_rect.right(), face_rect.bottom()))

        # Draw a box around each face we found
        win.add_overlay(face_rect)

        # Get the the face's pose
        pose_landmarks = face_pose_predictor(cap_image, face_rect)

        #print pose_landmarks.num_parts #print number of parts in object pose_landmarks, outputs 68
        print pose_landmarks.part(67)  #print particular landmark out of 0-67

        # Draw the face landmarks on the screen.
        win.add_overlay(pose_landmarks)
