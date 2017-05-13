from bs4 import BeautifulSoup as bs
import pandas as pd

soup = bs(open('C:\Users\dt85573\Desktop\imdb.htm', 'r'), 'html.parser')

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

df = pd.DataFrame(bdict)
print df

# df.to_csv(path_or_buf='C:\Users\dt85573\Desktop\imdb1.csv',sep='|',mode='w',encoding='utf-8')
