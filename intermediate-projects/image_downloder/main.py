from bs4 import BeautifulSoup as bs
import requests
import os
from PIL import Image
from io import BytesIO

userInput = input('Enter Your Search: ')
params = {'q':userInput}
url = 'https://www.bing.com/images/search'
page = requests.get(url,params=params)
soup = bs(page.content,'html.parser')
results =  soup.find('div', id="mmComponent_images_2")
# queryList =results.find_all('div', class_='img_cont')
imgClass =results.find_all('img', class_='mimg')

counter = 1 
for item in imgClass:
    img_Obj = requests.get(item['src'])
    print(item)
    title =f'{counter}.png'
    counter += 1

    # print(title)

    im = Image.open(BytesIO(img_Obj.content))
    im.save('./images/'+title,im.format)

