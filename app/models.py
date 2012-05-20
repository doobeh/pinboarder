from app import db
from datetime import datetime
from tools import generate_hash
from flask.ext.login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)

    def __init__(self, email, password):
        self.email = email.lower()
        self.password = password

    def __repr__(self):
        return "<%d : %s>" % (self.id, self.email)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    dt = db.Column(db.DateTime)
    author = db.Column(db.String(100))
    content = db.Column(db.Text)
    published = db.Column(db.Boolean, default=True)
    hash = db.Column(db.String(40))

    def __init__(self, data):
        self.author = data["a"]
        self.title = data["d"].encode('ascii','ignore')
        self.content = data["n"]
        self.url = data["u"]
        self.dt = datetime.strptime(data["dt"], '%Y-%m-%dT%H:%M:%SZ')
        self.hash = generate_hash(data["dt"], data["d"])

    def __repr__(self):
        return '<{title}>'.format(title=self.title)
