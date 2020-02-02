class Config:
    NEWS_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_TOP_URL ='https://newsapi.org/v2/everything?sources={}&apiKey={}'

class ProdConfig:
    pass


class DevConfig:
    DEBUG = True
