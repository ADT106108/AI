import requests
url = 'https://dct.ntcu.edu.tw/news.php'
html = requests.get(url)
html.encoding="utf-8"
print(html.text)

#把原始碼以每一列分割成串列，並去除跳列字元
htmllist = html.text.splitlines()
print(htmllist)

for roe in htmllist:
    print(row)

#統計個數
n=0
keyword = "數位"
for row in htmllist:
    if keyword in row: n+=1
print(  "找到 {} 次!" .format(n)  )

