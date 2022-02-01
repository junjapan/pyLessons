import requests
from bs4 import BeautifulSoup
import datetime
import time

#現在日付時刻の取得
dt_now = datetime.datetime.now()
dt_now_str = dt_now.strftime('%y%m%d')

#ファイル読み込み
with open('./in_path.txt','r',encoding='utf-8') as file:
    links=file.readlines()

print(links)

for link in links:
    res=requests.get(link.rstrip('\n'))
    res.encoding=res.apparent_encoding
    soup=BeautifulSoup(res.text,'html.parser')
    #曲名を取得
    title = soup.select('#mnb .cap h2')
    titleText = title[0].text.lstrip('「').rstrip('」歌詞')
    print(titleText)
    #歌詞を取得
    lyric = soup.select('.lbdy #Lyric')
    lyricText = lyric[0].get_text('\n')
    print(lyricText)
    print(f'{titleText}{dt_now_str}{links.index(link)}.txt')
    #ファイル書き込み
    with open(f'./{dt_now_str}_{links.index(link)}_{titleText}.txt','w',encoding='utf-8') as file:
         file.write(f'{lyricText}\n')
    #１秒空ける
    time.sleep(1)
