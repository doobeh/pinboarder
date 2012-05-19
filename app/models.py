from app import db
from datetime import datetime
from tools import generate_hash

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
        self.hash = generate_hash(data["dt"], data["d"])

    def __repr__(self):
        return '<{title}>'.format(title=self.title)
