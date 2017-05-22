import tweepy as tp
import os

consumer_key = 'l6ZdzW8HywA4oHW2cQgWUsjjn'
consumer_secret = '1azIWNFT4ci6taoc4NaSls0GoUo2ffM862WMipqSZ8LrnX2rzK'

access_token = '69954491-SZLB1VDk2Gq1YKDnBWLqgBm2kgPAQvYzdaCZD4BLb'
access_token_secret = 'QxKdl9FCh7xRurjvirTCzQXTefTQ8b3fALoguZlLAkD5j'


auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tp.API(auth)

# public_tweets = api.home_timeline()
# for tweets in public_tweets:
#     print tweets.text
# users = api.search_users('amitabh bacchan', verified = True)
# users = api.friends_ids('screen_name')

query='bhopal'

s = api.search(q=query,count= 20)

c =0

#print s

file = open(query+'.txt','w')

for i in s:
     c += 1
     #if i.entities['user_mentions']:
     if i.retweeted_status:
          #print i.entities['user_mentions'][0]['name']
          print i.retweeted_status.text
          #file.write(i.text.encode("utf-8").replace('\n','')+'\n')
     else:
          print i.text
          #file.write(i.text.encode("utf-8").replace('\n','')+'\n')

print c

print os.getcwd()