import requests
from bs4 import BeautifulSoup

res=requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding
#第1引数にhtml文字列,第2引数にパーサーを指定する。今回は追加ライブラリ不要な'html.parser'を指定
soup=BeautifulSoup(res.text,'html.parser')

#BeautifulSoupオブジェクトをprintにそのまま渡すと全文を表示する
#print(soup)

#タグで要素取得
ele=soup.find('title')
print(ele)
print(ele.text)

imgs=soup.find_all('img')
print(type(imgs))
for img in imgs:
    print(img.get('src'))

div=soup.find(id='headerImageBox')
print(type(div))

imgs=soup.select('.headerImage')
for img in imgs:
    print(img.get('src'))

eles=soup.select('tbody td:first-child')
#先生からの提示例
#eles=eles[0:len(eles):3]
for ele in eles:
    print(ele.text)

links=soup.select('li a')

with open('zoo.txt','w',encoding='utf-8') as file:
    for link in links:
        file.write(f'{link.text}:{link.get("href")}\n')

