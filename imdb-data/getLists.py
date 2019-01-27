import sys
import numpy as np
import os
import json

original_paths = []

for i in range (0,10):
        directory = 'D:\\imdb_crop\\imdb_crop\\0' + str(i)
        for filename in os.listdir(directory):

            imagePath = directory + '\\' + filename
            original_paths.append(imagePath)

for i in range (10,100):
    directory = 'D:\\imdb_crop\\imdb_crop\\' + str(i)
    for filename in os.listdir(directory):

        imagePath = directory + '\\' + filename
        original_paths.append(imagePath)

with open('lists.json', 'w') as output:
    json.dump(original_paths, output)
