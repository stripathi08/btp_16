import face_recognition
import cv2
import os, sys
from os import listdir
import dlib

video_capture = cv2.VideoCapture(0)

def calc_track_loc(top, left, bottom, right):
    track_x = (left + right) / 2
    track_y = (top + bottom) / 2
    return (track_x, track_y)

def recognize_people(people_folder):


    # Define variables
    sample_face_encoding = []

    # Load all sample picture from directory ./sample_faces and learn how to recognize it.
    sample_list = listdir(people_folder)
    print "these are the people in database:"
    for file_name in sample_list:
        print file_name
        this_image = face_recognition.load_image_file("sample_faces/" + file_name)
        sample_face_encoding.append(face_recognition.face_encodings(this_image)[0])

    # Initialize some variables
    face_locations = []
    face_encodings = []
    # face_names = []
    process_this_frame = 0

    while True:

        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)

        # Only process every other frame of video to save time
        if process_this_frame % 5 == 0:
            track_locs = []
            face_names = []

            # Find all the sample_faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(
                small_frame)  # list of faces locations # Face detection Algo 1
            face_encodings = face_recognition.face_encodings(small_frame,
                                                             face_locations)  # list of face encoding arrays # Face encoding extraction Algo 2

            for face_encoding in face_encodings:  # face encoding is a 1x128 array
                # See if the face is a match for the known face(s)
                match = face_recognition.compare_faces(sample_face_encoding,
                                                       face_encoding)  # Encoding comparison Algo 3
                name = "u"

                for i, sample_name in enumerate(sample_list):
                    if match[i]:
                        name = sample_name[0]

                face_names.append(name)
                # print face_names

            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                track_locs.append(calc_track_loc(top, left, bottom, right))
                # Draw a box around the face
                # print track_locs

                final_track_locs = []
                for elem in xrange(len(track_locs)):
                    final_track_locs.append(
                        str(int(track_locs[elem][0]) + int(100)) + str(int(track_locs[elem][1]) + int(100)) + str(0))
                    # final_track_locs = str(track_locs[0][0]) + str(track_locs[0][1])
                    # print final_track_locs
            assert len(track_locs) == len(face_names), "Error in comparison"
        process_this_frame += 1

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)  # Blue Rectangle with thickness 2

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        if process_this_frame % 25 == 0:
            try:
                sending_information(final_track_locs)
            except:
                pass

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

def add_person(people_folder):
    person_name = raw_input("Enter person name :").lower()

    while True:
        ret, frame = video_capture.read()
        cv2.imwrite(people_folder+'/'+person_name+'.jpg', frame)
        cv2.imshow("capturing frame ", frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


def check_choice():
    validity = 0
    if not validity:
        try:
            choice = int (raw_input("Enter your choice:"))
            if choice in [1,2,3]:
                validity = 1
            else:
                print "%d is not an option " % choice
        except ValueError, error:
            print "%s is not an option.\n" % str(error).split(": ")[1]
        return choice

if __name__== "__main__":

    print "------Program for Face recognition------\n"
    print "1. Add people\n2. Start face recognizer\n3. Exit program\n"

    CHOICE = check_choice()
    PEOPLE_FOLDER = "sample_faces"

    if CHOICE == 1:
        if not os.path.exists(PEOPLE_FOLDER):
            os.makedirs(PEOPLE_FOLDER)
        add_person(PEOPLE_FOLDER)
    elif CHOICE == 2:
        recognize_people(PEOPLE_FOLDER)
    elif CHOICE == 3:
        sys.exit()