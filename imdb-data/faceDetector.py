import cv2
import sys
import numpy as np
import os
import csv

image_list = []

while (len(image_list) < 30000):
    for i in range (0,10):
        directory = 'D:\\imdb_crop\\imdb_crop\\0' + str(i)

        for filename in os.listdir(directory):

            imagePath = directory + '\\' + filename
            cascPath = sys.argv[1]

            faceCascade = cv2.CascadeClassifier(cascPath)

            image = cv2.imread(imagePath)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize=(30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
            )

            padding = 20

            print("Found {0} faces!".format(len(faces)))
            if (len(faces) == 1):
                for (x, y, w, h) in faces:
                    cv2.rectangle(image, (x-padding, y-padding), (x + w + padding, y + h + padding), (0, 255, 0), 2)
                    sub_face = image[y:y+h, x:x+w]
                    resize_image = cv2.resize(sub_face, (64,64))
                if ((((y + h) - y) > 64) and ((x + w) - x) > 64):
                #Check if sub_face size is greater than 150x150, if this is true place the filename in the list
                    cv2.imwrite('D:\\new_images\\' + filename, resize_image)
                    image_list.append('D:\\new_images\\' + filename)
                    cv2.waitKey(0)

    for i in range (10,100):
        directory = 'D:\\imdb_crop\\imdb_crop\\' + str(i)

        for filename in os.listdir(directory):

            imagePath = directory + '\\' + filename
            cascPath = sys.argv[1]

            faceCascade = cv2.CascadeClassifier(cascPath)

            image = cv2.imread(imagePath)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize=(30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
            )

            padding = 20

            print("Found {0} faces!".format(len(faces)))
            if (len(faces) == 1):
                for (x, y, w, h) in faces:
                    cv2.rectangle(image, (x-padding, y-padding), (x + w + padding, y + h + padding), (0, 255, 0), 2)
                    sub_face = image[y:y+h, x:x+w]
                    resize_image = cv2.resize(sub_face, (64,64))
                #Check if sub_face size is greater than 150x150 if true place filename in list
                if ((((y + h) - y) > 64) and ((x + w) - x) > 64):
                    cv2.imwrite('D:\\new_images\\' + filename, resize_image)
                    image_list.append('D:\\new_images\\' + filename)
                    cv2.waitKey(0)