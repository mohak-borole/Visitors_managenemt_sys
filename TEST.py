
import cv2
from simple_facerec import SimpleFacerec

class FaceRecognizer:
    def __init__(self):
        sfr = SimpleFacerec()
        sfr.load_encoding_images("dataset/")

    def faceRecognition(self):
        sfr = SimpleFacerec()
        # Load Camera
        cap = cv2.VideoCapture(0)
        name = ""
        while True:
            ret, frame = cap.read()

            # Detect Faces
            face_locations, face_names = sfr.detect_known_faces(frame)
            if len(face_locations) == 0:
                continue
            # Create a list of threads
            threads = []
            for face_loc, name in zip(face_locations, face_names):
                # Create a thread to recognize the face
                thread = Thread(target=self._recognize_face, args=(face_loc, name , frame))
                threads.append(thread)

            # Start all of the threads
            for thread in threads:
                thread.start()

            # Wait for all of the threads to finish
            for thread in threads:
                thread.join()

            if name != "" and self.sfr.confidence(face_loc) > 75:
                break

        cap.release()
        cv2.destroyAllWindows()
        return name

    def _recognize_face(self, face_loc, name , frame):
        # Crop the face from the frame
        face = frame[face_loc[0]:face_loc[2], face_loc[1]:face_loc[3]]

        # Recognize the face
        name = self.sfr.recognize_face(face)

        # Draw a rectangle around the face
        cv2.rectangle(frame, (face_loc[1], face_loc[0]), (face_loc[3], face_loc[2]), (0, 0, 200), 4)
        # Write the name of the person to the frame
        cv2.putText(frame, name, (face_loc[1], face_loc[0] - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.imshow("Visitors Management System", frame)

detector = FaceRecognizer
Name = detector.faceRecognition(detector)
print(Name)
