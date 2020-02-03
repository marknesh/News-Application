from app import app
from flask import render_template,redirect,url_for,request


from .requests import get_news,get_headlines,get_search,get_topstories
@app.route('/')
def headline():

    newsources = get_news()
    toplines=get_topstories('us')
    search_url= request.args.get('search_article')
    if search_url:
        return redirect(url_for('search',query=search_url))
    else:
        return render_template('index.html', source=newsources,headlines=toplines)

@app.route('/sources/<sources>')
def index(sources):
    topheadline = get_headlines(sources)
    title = 'Welcome to the news website'
    return render_template('news.html', title = title,heads=topheadline)


@app.route('/search/<query>')
def search(query):
    search_list=query.split(" ")
    new_search="+".join(search_list)
    newst=get_search(new_search)
    if newst:
        return render_template('search.html',search=newst)
    else:
        return render_template('blank.html')

@app.errorhandler(404)
def err(error):

    return render_template('error.html'),404

