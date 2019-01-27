import json 

def getAges():

    with open('date_of_birth.txt') as readFile:
        yeet_dabs = readFile.read()
    list_of_yeet = yeet_dabs.split('\t')
    print(len(list_of_yeet))

    with open('date_of_photo.txt') as readFile:
        years = readFile.read()
    list_of_year = years.split('\t')
    print(len(list_of_year))

    ages = []

    for i in range (len(list_of_yeet)):
        ages.append(int(int(list_of_year[i]) - (int(list_of_yeet[i]) / 365.25)))

    print(ages)
    with open('ages.json', 'w') as output:
        json.dump(ages, output)
    return ages
getAges()