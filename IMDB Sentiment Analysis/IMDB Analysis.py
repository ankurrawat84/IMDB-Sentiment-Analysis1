from bs4 import BeautifulSoup as bs
import pandas as pd
import tweepy as tp
import requests as rq
import os


def sentimentcalc(subj):
    posfile = open('/Users/ankurrawat/PycharmProjects/Practice/Practice1/positive-words.txt', 'r')
    negfile = open('/Users/ankurrawat/PycharmProjects/Practice/Practice1/negative-words.txt', 'r')

    poslist = []
    neglist = []

    for words in posfile:
        poslist.append(words.replace('\n', ''))

    for words in negfile:
        neglist.append(words.replace('\n', ''))

    posset = set(poslist)
    negset = set(neglist)

    tweetfile = open('/Users/ankurrawat/PycharmProjects/IMDB-Sentiment-Analysis/IMDB Sentiment Analysis/' + subj + '.txt', 'r')

    sentanal = {}

    for sentence in tweetfile:
        poscount = 0
        negcount = 0
        words = sentence.split()
        for word in words:
            if word in posset:
                poscount += 1
            elif word in negset:
                negcount += 1
            else:
                continue
        if poscount > negcount:
            sentiment = 'positive'
        elif negcount > poscount:
            sentiment = 'negetive'
        else:
            sentiment = 'netural'

        sentanal[sentence] = sentiment

    finalsentimentcount = 0

    for senti in sentanal.values():
        if senti == 'negetive':
            finalsentimentcount -= 1
        elif senti == 'positve':
            finalsentimentcount += 1
        else:
            finalsentimentcount += 0

    if finalsentimentcount > 0:
        return 'Positve Sentiment'
    elif finalsentimentcount < 0:
        return 'Negetive Sentiment'
    else:
        return 'Neutral Sentiment'

def WebScrape():

    soup = bs(rq.get('http://www.imdb.com/search/name?birth_monthday=05-20').text, 'html.parser')
    cnt = 0
    bdict = {}
    name, image, proff, best = [], [], [], []
    f = soup.table.find_all('tr')
    for i in f:
        if i.a.get('title'):
            name.append(i.a.get('title'))
            image.append(i.a.img.get('src'))
            proff.append(i.span.contents[0])
            best.append(i.span.a.string)
        else:
            continue
    bdict['Name'], bdict['image'], bdict['proff'], bdict['best'] = name, image, proff, best
    while cnt < len(bdict['Name']):
        yield [bdict['Name'][cnt],bdict['image'][cnt],bdict['proff'][cnt],bdict['best'][cnt]]
        cnt += 1

def twitterpull(subj):

    consumer_key = 'l6ZdzW8HywA4oHW2cQgWUsjjn'
    consumer_secret = '1azIWNFT4ci6taoc4NaSls0GoUo2ffM862WMipqSZ8LrnX2rzK'

    access_token = '69954491-SZLB1VDk2Gq1YKDnBWLqgBm2kgPAQvYzdaCZD4BLb'
    access_token_secret = 'QxKdl9FCh7xRurjvirTCzQXTefTQ8b3fALoguZlLAkD5j'

    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tp.API(auth)

    s = api.search(q=subj, count=100)

    c = 0
    file = open(subj + '.txt', 'w')
    for i in s:
        c += 1
        if i.text:
            file.write(i.text.encode("utf-8").replace('\n','')+'\n')
        else:
            continue

for info in WebScrape():
    twitterpull(info[0])
    print 'Name: '+info[0]
    print 'Image: '+info[1]
    print 'Best Work: ' + info[2]
    print 'Proffessional: ' + info[1]
    print 'Sentiment: ' + sentimentcalc(info[0])


