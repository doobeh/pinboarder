import os
_basedir = os.path.abspath(os.path.dirname(__file__))

ADMIN = {'email':'admin@example.com', 'password':'secretkey'}
SECRET_KEY = 'SecretKeyForSessionSigning'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
PAGINATION_PAGES = 5
FEED_URL = r'http://feeds.pinboard.in/json/v1/u:yayitsrob/t:design/'