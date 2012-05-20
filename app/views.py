from app import db, app
from flask import render_template, request, flash, redirect, url_for
from forms import LoginForm, EditForm
from models import User, Post
from flask.ext.login import login_required, current_user, login_user, logout_user
from app import login_manager
from tools import generate_hash
import urllib2
import simplejson

@app.route('/', defaults={'page': 1})
@app.route('/archive/<int:page>/')
def home(page=1):
    posts = Post.query.filter_by(published=True).order_by(Post.dt.desc()).paginate(page,app.config["PAGINATION_PAGES"])
    return render_template('home.html',pagination=posts, endpoint_func=lambda x: url_for('home',page=x))

@app.route('/manage/')
@login_required
def manage():
    p = Post.query.order_by(Post.dt.desc()).all()
    return render_template("manage.html", posts=p, user=current_user)

@app.route('/manage/pull/')
@login_required
def pull_feed():
    req = urllib2.Request(app.config["FEED_URL"])
    opener = urllib2.build_opener()
    f = opener.open(req).read()
    results = simplejson.loads(f)
    for post in results:
        if not Post.query.filter_by(hash=generate_hash(post["dt"],post["d"])).first():
            db.session.add(Post(post))
            print Post
            db.session.commit()
    return redirect(url_for('manage'))

@app.route('/manage/flip/<id>/')
@login_required
def flip_published(id):
    post = Post.query.filter_by(id=id).first_or_404()
    if post.published:
        post.published = False
    else:
        post.published = True
    db.session.commit()
    return redirect(url_for('manage'))

@app.route('/manage/edit/<int:id>',methods=['GET','POST'])
def edit_post(id):
    post = Post.query.filter_by(id=id).first_or_404()
    form = EditForm(obj=post)
    if form.validate_on_submit():
        print "weee"
        form.populate_obj(post)
        db.session.commit()
        return redirect(url_for('manage'))
    return render_template('edit_post.html', form=form)


## Login Related ##


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User.query.filter_by(id=userid).first()

@app.route('/login/', methods=['GET', 'POST'])
def login():
    """
    Login form
    """
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Welcome %s' % user.email)
            return redirect(url_for('home'))
        flash('Wrong email or password', 'error-message')
    return render_template("login.html", form=form)

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('home'))