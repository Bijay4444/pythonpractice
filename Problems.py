import requests
from bs4 import BeautifulSoup

source = requests.get('https://coreyms.com').text
soup = BeautifulSoup(source, 'html5lib')

for article in soup.find_all('article'):

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    vid_src = article.find('iframe', class_ ="youtube-player")['src']

    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]

    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(yt_link)

    print()
