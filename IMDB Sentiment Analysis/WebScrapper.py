from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd

# #htl = rq.request('http://www.imdb.com/search/name?birth_monthday=05-20')
#
# #soup = bs(open('C:\Users\dt85573\Desktop\imdb.htm', 'r'), 'html.parser')
#
# soup = bs(rq.get('http://www.imdb.com/search/name?birth_monthday=05-20').text, 'html.parser')
#
# bdict = {}
# name, image, proff, best = [], [], [], []
#
# f = soup.table.find_all('tr')
#
# for i in f:
#     if i.a.get('title'):
#         name.append(i.a.get('title'))
#         image.append(i.a.img.get('src'))
#         proff.append(i.span.contents[0])
#         best.append(i.span.a.string)
#     else:
#         continue
#
# bdict['Name'], bdict['image'], bdict['proff'], bdict['best'] = name, image, proff, best
#
# df = pd.DataFrame(bdict)
# print df
#
# # df.to_csv(path_or_buf='C:\Users\dt85573\Desktop\imdb1.csv',sep='|',mode='w',encoding='utf-8')

def WebScrapper():
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




for info in WebScrapper():
    print info


