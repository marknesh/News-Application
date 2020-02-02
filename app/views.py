from app import app
from flask import render_template,redirect,url_for


from .requests import get_news,get_headlines
@app.route('/')
def headline():
    newsources = get_news()

    return render_template('index.html',source=newsources)

@app.route('/<sources>')
def index(sources):
    #
    # newsources = get_news()
    topheadline = get_headlines(sources)



    title = 'Welcome to the news website'
    return render_template('news.html', title = title,heads=topheadline)


