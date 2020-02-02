from app import app
import urllib.request, json
from .models import news
from .models.news import Article

News = news.News


api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_BASE_URL']
top_url = app.config['NEWS_TOP_URL']


def get_news():
    news_url = base_url.format(api_key)
    with urllib.request.urlopen(news_url) as url:
        news_data = url.read()
        new_news = json.loads(news_data)

        if new_news['sources']:
            source_news = new_news['sources']
            news_sources = process_news(source_news)

    return news_sources


def process_news(news_list):


    news_sources = []
    for newss in news_list:

        name = newss.get('name')
        id = newss.get('id')
        linkurl = newss.get('url')
        des = newss.get('description')

        if name:
            sourcesfornews = News(name,id,linkurl,des)
            news_sources.append(sourcesfornews)

    return  news_sources


def get_headlines(sources):
    headlines = top_url.format(sources,api_key)

    with urllib.request.urlopen(headlines) as urls:
        headlineurl= urls.read()
        urlforheadlines= json.loads(headlineurl)

        if urlforheadlines['articles']:
            headurl= urlforheadlines['articles']
            Head=process_headline(headurl)

    return Head


def process_headline(new_list):

    topHeadline=[]

    for top in new_list:
        id= top.get('id')
        nameheadline=top.get('title')
        image = top.get('urlToImage')
        link = top.get('url')
        timepublished = top.get('publishedAt')
        description = top.get('description')

        if image:
            head=Article(id,nameheadline,image,link,timepublished,description)
            topHeadline.append(head)
    return topHeadline











