
posfile = open('/Users/ankurrawat/PycharmProjects/Practice/Practice1/positive-words.txt', 'r')
negfile = open('/Users/ankurrawat/PycharmProjects/Practice/Practice1/negative-words.txt', 'r')

poslist = []
neglist = []

for words in posfile:
    poslist.append(words)

for words in negfile:
    neglist.append(words)

posset = set(poslist)
negset = set(neglist)


tweetfile = open('/Users/ankurrawat/PycharmProjects/Practice/Practice1/bhopal.txt','r')

sentanal = {}

for sentence in tweetfile:

    poscount = 0
    negcount = 0
    words = sentence.split()
    for word in words:
        print word
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

        sentanal['Sentence']= sentence
        sentanal['Emotion'] = sentiment

print sentanal













