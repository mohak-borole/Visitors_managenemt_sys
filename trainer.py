import cv2
import numpy as np
from PIL import Image
import os

# Path for face image data base
path = 'dataset'

# Create Local Binary Patterns Histograms recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the cascade classifier for detecting faces
detector = cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")

# Function to get the images and label data
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:
        # Load image in grayscale
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img,'uint8')

        # Extract the user name from the file name
        name = os.path.split(imagePath)[1].split(".")[1]
        
        # Convert user name to an integer id
        id = int.from_bytes(name.encode(), 'little')
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids

print ("\nTraining faces. It will take a few seconds. Wait ...")

# Get the face samples and ids from the dataset
faces,ids = getImagesAndLabels(path)

# Train the recognizer on the face samples
recognizer.train(faces, np.array(ids))

# Save the model into trainer/trainer.yml
recognizer.write('trainer/trainer.yml') 

# Print the number of faces trained and end program
print("\n {0} faces trained. Exiting Program".format(len(np.unique(ids))))
