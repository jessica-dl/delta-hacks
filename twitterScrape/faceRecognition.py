import cv2
import sys
import numpy as np
import os



directory = 'pictures/'

for filename in os.listdir(directory):

    imagePath = directory + filename
    cascPath = sys.argv[1]

    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 10,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    padding = 20
    if (len(faces) >= 1 and len(faces) < 4):
        print("Found {0} faces!".format(len(faces)))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x-padding, y-padding), (x + w + padding, y + h + padding), (0, 255, 0), 2)
            if (((y + h) - y) >= 64 and ((x + w) - x) >= 64):
                sub_face = image[y:y+h, x:x+w]
                sub_face_file = "subfaces/" + filename
                resize_image = cv2.resize(sub_face, (64, 64))
                cv2.imwrite(sub_face_file, resize_image)



            #cv2.imwrite('newpictures/' + filename, image)
            #cv2.waitKey(0)
