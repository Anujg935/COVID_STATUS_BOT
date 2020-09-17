from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as soup
import time

news_link = "https://economictimes.indiatimes.com/news/politics-and-nation/coronavirus-cases-in-india-live-news-latest-updates-march27/liveblog/74838380.cms"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


def getNewsHeadlines():
    req = Request(url=news_link, headers=headers) 
    html = urlopen(req).read() 
    html_soup = soup(html,"html.parser")

    eachStory = html_soup.findAll("div",{'class':'eachStory'})
    headlines = []
    for f in eachStory:
        headline = f.findAll("h3",{'class':''})
        if(headline== None):
            continue;
        else:
            headline = f.findAll("h3",{'class':''})
            for h in headline:
                #print(h.text)
                if(len(h.text) != 0):
                    timeStamp = f.findAll("div",{'class':'timeStamp'})
                    for t in timeStamp:
                        s = t.findAll("span",{'class':''})
                        for s in t:
                            #print(s.text)
                            headlines.append("<b>"+s.text+"</b>"+" "+h.text)
    del headlines[1::2]
    return headlines