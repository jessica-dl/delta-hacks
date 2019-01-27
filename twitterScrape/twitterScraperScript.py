


import tweepy
import csv
import pandas as pd
import wget
####input your credentials here
consumer_key = 'here'
consumer_secret = 'here'

access_token = 'here'
access_token_secret = 'here'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
media_files = []
i = 0
for tweet in tweepy.Cursor(api.search,q="#TenYearChallenge",count=20000, lang="en", since="2018-05-01", include_entities = True).items():
    if 'RT @' not in tweet.text and 'media' in tweet.entities and 'video' not in tweet.entities :
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
        media = tweet.entities.get('media', [])
        if (len(media) > 0):
            for picture in media :
                media_files.append(picture['media_url'])
                i += 1

        if (i >= 20000):
            break

a = 0
print(media_files)
for media_file in media_files:
    wget.download(media_file, 'pictures/image' + str(a) + '.jpg')
    a += 1


csvFile.close()
