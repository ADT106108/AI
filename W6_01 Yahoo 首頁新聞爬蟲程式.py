import requests
from bs4 import BeautifulSoup

#下載網頁內容
r = requests.get('https://tw.yahoo.com/')

#確認是否下載成功
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    stories = soup.find_all('a', class_='story-title')
    for s in stories:
     print("標題:" + s.text)
     print("網址:" + s.get('href'))
     