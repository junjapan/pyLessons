import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

load_url='http://www.higashiyama.city.nagoya.jp/04_zoo/friend/2018/02/post-21.html'
res=requests.get(load_url)
res.encoding=res.apparent_encoding
soup=BeautifulSoup(res.text,'html.parser')

#フォルダ作成
out_folder=Path('dl_eastImg')
out_folder.mkdir(exist_ok=True)

imgs=soup.select('#slider1 img')

for img in imgs:
    src=img.get('src')
    img_url=urllib.parse.urljoin(load_url,src)

    loaded_img=requests.get(img_url)
    file_name=src.split('/')[-1]
    out_path=out_folder.joinpath(file_name)
    print(out_path)
    with open(out_path,'wb') as file:
        file.write(loaded_img.content)

    time.sleep(1)
