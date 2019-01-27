# Ten Year Challenge Neural Net

## Inspiration and what it does
The 10 Year Challenge has been blowing up on social media for the last couple months. People have been posting photos of themselves from ten years ago, and seeing how they've changed by putting it next to a photo of them from this year. There has been a lot of discussion about the reasoning behind the popularity of this "challenge"- one of the most known theories being that Facebook has been using the data to train their algorithms. 

We decided to do just that- scrape data from online to train a neural network to age a face based on a given photo. We wanted to show that Facebook doesn't actually need people's ten year challenge data to train their models. 

## How we built it
The main components of this project are the neural net and the data scraper. We wrote a neural net to age the photos using Keras in Python. We got our data from two different sources- a script that scraped data from Twitter and an IMdb database of celebrity photos. We then had to analyze the datasets to ensure that we only took photos that had usable information- specifically photos that had a face that took up at least 50% of the photo's area. Those photos then had be formatted so that the neural net could train on it.

## Challenges we ran into
We ran into a lot of challenges while working with the GCP platform, when we were trying to set up a server with a GPU. This turned out to be the first of many issues with our project. Getting the photos in the correct format for training the net also created a difficult challenge. We had to ensure that the pictures were being properly cropped and parsed, and then had to run through over 30,000 of them before sending them to the neural net. This caused problems (we may have not saved it the first time we ran it...) and we ran out of time to properly train the net. 

## Accomplishments that we're proud of
Hopefully it works? We'll be proud if it does.

## What's next for Ten Year Challenge (Does FB want your data?)
Make it functional.

### Credits
[This paper](https://arxiv.org/pdf/1702.01983.pdf) blessed us, although it was missing vital information, so we created our own design for encoding and decoding the images.## Inspiration and what it does
The 10 Year Challenge has been blowing up on social media for the last couple months. People have been posting photos of themselves from ten years ago, and seeing how they've changed by putting it next to a photo of them from this year. There has been a lot of discussion about the reasoning behind the popularity of this "challenge"- one of the most known theories being that Facebook has been using the data to train their algorithms. 

We decided to do just that- scrape data from online to train a neural network to age a face based on a given photo. We wanted to show that Facebook doesn't actually need people's ten year challenge data to train their models. 

## How we built it
The main components of this project are the neural net and the data scraper. We wrote a neural net to age the photos using Keras in Python. We got our data from two different sources- a script that scraped data from Twitter and an IMdb database of celebrity photos. We then had to analyze the datasets to ensure that we only took photos that had usable information- specifically photos that had a face that took up at least 50% of the photo's area. Those photos then had be formatted so that the neural net could train on it.

## Challenges we ran into
We ran into a lot of challenges while working with the GCP platform, when we were trying to set up a server with a GPU. This turned out to be the first of many issues with our project. Getting the photos in the correct format for training the net also created a difficult challenge. We had to ensure that the pictures were being properly cropped and parsed, and then had to run through over 30,000 of them before sending them to the neural net. This caused problems (we may have not saved it the first time we ran it...) and we ran out of time to properly train the net. 

## Accomplishments that we're proud of
Hopefully it works? We'll be proud if it does.

## What's next for Ten Year Challenge (Does FB want your data?)
Make it functional.

### Credits
[This paper](https://arxiv.org/pdf/1702.01983.pdf) blessed us, although it was missing vital information, so we created our own design for encoding and decoding the images.

Created by Sam Cymbaluk, Alex Samaha and Jessica de Leeuw
