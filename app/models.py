from app import db
from datetime import datetime
import hashlib

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    dt = db.Column(db.DateTime)
    author = db.Column(db.String(100))
    content = db.Column(db.Text)
    published = db.Column(db.Boolean, default=True)
    hash = db.Column(string(40))

    def __init__(self, data):
        self.author = data["a"]
        self.title = data["d"]
        self.url = data["u"]
        self.dt = datetime.strptime(data["dt"], '%Y-%m-%dT%H:%M:%SZ')

        hash = hashlib.sha1()
        hash.update(data["d"])
        hash.update(data["dt"])
        self.hash = hash

    def __repr__(self):
        return '<{title}>'.format(title=self.title)
