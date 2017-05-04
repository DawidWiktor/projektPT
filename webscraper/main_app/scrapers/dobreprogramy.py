# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from pytz import timezone  # python timezones
import queue

ARTICLES = queue.Queue()
END = False

def dobreprogramy_date2_python_date(date):
    date = date.split(".")  # [24, 04, 2017 1:27]
    day = date[0]
    month = date[1]
    date = date[2].split(" ")  # # [2017, 1:27]
    year = date[0]
    date = date[1].split(":")
    hours = date[0].zfill(2)
    minutes = date[1]
    together = day + " " + month + " " + year + " " + hours + ":" + minutes
    try:
        datetime_object = datetime.strptime(together, '%d %m %Y %H:%M')
        datetime_object = datetime_object.replace(tzinfo=timezone('Europe/Warsaw'))
    except ValueError:
        datetime_object = ""
    return datetime_object

def main_articles(pages):
    global ARTICLES
    for page in range(1, pages + 1):
        webpage = requests.get("https://www.dobreprogramy.pl/Blog,"+str(page)+".html")
        soup = BeautifulSoup(webpage.text, 'lxml')

        print("Page: " + str(webpage.url))
        # start scraping
        dobreprogramy = soup.find_all('article')
        for i in dobreprogramy:
            if i.header is None:
                continue
            else:
                title = i.header.h1.a.text
                author = i.find(class_="content-info").find('a', rel='author').text
                link = i.header.h1.a['href']
                date = i.find(class_="content-info").time.text
                date = dobreprogramy_date2_python_date(date)
                text = i.find(class_="entry-content").text

                page1 = requests.get(link)  # have to open page for scrap all tags
                soup1 = BeautifulSoup(page1.content, 'lxml')

                artykul = soup1.find(class_='tags font-heading-master')
                tags = ', '.join([i.text for i in artykul.find_all('a')])

                page2 = requests.get("https://www.dobreprogramy.pl/"+author)
                soup2 = BeautifulSoup(page2.content, 'lxml')
                image = soup2.find_all("img", alt="avatar")
                try:
                    imagelink = image[0].attrs['src']
                except IndexError:
                    # I don't know why sometimes scraper can't find this img
                    imagelink = "https://static.dpcdn.pl/res/default.jpg"
                    #print("\t" + link)

                one_article = {"title": title, "date": date, "author": author, "link": link,
                               "tags": tags, "text": text, "imageLink": imagelink}
                ARTICLES.put(one_article)


def scrapshot(pages):
    global END
    main_articles(pages)
    END = True

if __name__ == "__main__":
    scrapshot(pages)
