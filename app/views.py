from app import db, app

@app.route('/')
def home():
    return 'OK'
