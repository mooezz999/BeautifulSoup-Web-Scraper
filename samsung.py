
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('Samsungebayfrom7.csv', 'w',encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=samsung&_sacat=0&LH_TitleDesc=0&_pgn='
file = open('Samsungebayfrom7.json','w',encoding='utf8')
file.write('[\n')
data = {}
csv_columns = ['name','price','img']
for page in range(1000):
    print('---', page, '---')
    r = requests.get(url + str(page) +'&rt=nc')
    print(url + str(page))
    print(r.content)
    soup = BeautifulSoup(r.content, "html.parser")
    ancher=soup.find_all('div',{'class' : 's-item__wrapper clearfix'})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i=0
    writer.writeheader()
    for pt in  ancher:
        name=pt.find('h3', {'class' : 's-item__title'})
        itemPrice=pt.find('span', {'class' : 's-item__price'})
        img=pt.find('img', {'class' : 's-item__image-img'})
        
        if img:      
            writer.writerow({'name': name.text.replace('                    ', '').strip('\r\n'), 'price': itemPrice.text, 'img': img.get('src')})
            data['name'] =name.text.replace('                    ', '').strip('\r\n')
            data['price'] =itemPrice.text
            data['img'] =img.get('src')
            json_data = json.dumps(data,ensure_ascii=False)
            file.write(json_data)
            file.write(",\n")             
file.write("\n]")
filecsv.close()
file.close()