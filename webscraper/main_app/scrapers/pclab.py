# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import threading
from pytz import timezone
import queue

ARTICLES = queue.Queue()
END = False

def pclab_date2_python_date(date):
    day, month, year = date.split(".")
    together = day + " " + month + " " + year
    try:
        datetime_object = datetime.strptime(together, '%d %m %Y')
        datetime_object = datetime_object.replace(tzinfo=timezone('Europe/Warsaw'))
    except ValueError:
        raise
    return datetime_object

def main_articles(pages):
    global ARTICLES
    for page in range(1, pages + 1):
        webpage = requests.get("http://pclab.pl/news-" + str(page) + ".html")
        soup = BeautifulSoup(webpage.content, 'lxml')

        print("Page: " + str(webpage.url))

        pclab = soup.find_all(class_="element")
        for i in pclab:
            try:
                link = "http://pclab.pl" + i.find(class_="title").a['href']
                text = i.find(class_="text").p.text
                title = i.find(class_="title").a.text
                temp_info = i.find(class_="info").text
                author, date, c, d = temp_info.split("|")
                date = date[1:-1]
                date = pclab_date2_python_date(date)
                image_link = " http://pclab.pl" + i.find(class_="text").a.img['src']
                tags = i.find(class_="tags").text
                a, tags = tags.split("Tagi:")
            except:
                print("Error:", link)
                continue

            tags_list = []
            for tmp in tags.split(","):
                tmp = tmp.replace("\n","")
                if tmp[0] == " ":
                    tmp = tmp[1:]
                if tmp[-1] == " ":
                    tmp = tmp[:-1]

                tags_list.append(tmp)

            one_article = {"title": title, "date": date, "author": author, "link": link,
                           "tags": tags_list, "text": text, "image_link": image_link}
            ARTICLES.put(one_article)


def test():
    while not ARTICLES.empty():
        i = ARTICLES.get()
        print(i['tags'])

def scrapshot(pages):
    global END
    main_articles(pages)
    END = True

if __name__ == "__main__":
    scrapshot(pages)
