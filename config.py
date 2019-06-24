import os

class Config:

   	NEWS_SOURCES _BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'
   	ARTICLES_ BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
   	NEWS_AP I_KEY = os.environ.get('NEWS_API_KEY')
    # SECRET_KEY = os.environ.get('SECRET_KEY')
   	@staticmethod
   	def init_app(app):
   		pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
