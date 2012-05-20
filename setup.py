from app import db, app
from app.models import *

db.drop_all()
db.create_all()

u = User('admin@example.com','password')

db.session.add(u)
db.session.commit()