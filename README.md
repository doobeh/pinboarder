# Pinboarder

### In short
Pinboarder turns a [Pinboard][pinboard] feed into a mostly functional Blog system.

### But why?!
[Pinboard.in][pinboard] is a social bookmarking site that gathers and keeps your
favourite links in order.  It makes sense that if you're already collecting the
best of the web in one place, then if you want to start a curation type blog, and
keep it up to date, being able to tie the blog system into your Pinboard account would
seem like a very good idea indeed.

### So, how does it work?
Pinboard has a very accessible API, if you want to view all the shared links from
"Chaos", well you can just go to
[http://feeds.pinboard.in/json/v1/u:chaos][1] and you'll get a nice json stream
of all the posts.  Further, if you wish to only view posts tagged with "Apple"
you can simply go to [http://feeds.pinboard.in/json/v1/u:chaos/t:Apple/][2].

What Pinboarder does is create a small database, and then queries Pinboard
for all the posts at a particular feed, it runs down the list and creates
entries for all the bookmarked posts.  Then you can just login to the admin
side of the site and manage the posts, edit the content here and there (by
default it'll pull in the Pinboard notes) or even the Title if it needs a
tweak or two.

It also creates a unique hash of each of the posts, so even if you change
the title, it will know not to import the old one next time you run an
update.

### Hmm, okay, so.. how do I run it?
* Git clone the repository to your computer
* Create a Python virtual environment and activate it
* Install the requirements (```pip install -r requirements.txt```)
* Setup the server ```setup.py````
* Run the server ```rundebug.py````
* Access the site at [http://127.0.0.1:5000][3]

I'll add a better deployment mechanism so you can very easily deploy an instance
to the wonderful Heroku.

### Anything else?
I shall be documenting this project on my site soon, and I'll leave a link here
when I do-- mostly as a tutorial for new people coming into the Flask web
development framework.

Lots of tweaks required too in the not too distant future--
* The pinboard refresh function is fired on request at the
moment, it should run automatically in the background really.
* The Feed url is hardcoded in the ```config.py``` file at the moment, I should
move that into the admin interface.
* Limited querying of Pinboard.  At present when a update is requested, all the
posts matching are returned, if a user had thousands of posts that would be a bit
unfair to Pinboard.  Instead it should memorize the last sucessful update, then
just ask the Pinboard API for all posts newer than that time.
* Improve the user interface so it's a working theme that someone might actually
want to use
* Add a few blueprints to break the site apart, at least to document in the
tutorial to make it a more complete introduction.

[1]: http://feeds.pinboard.in/json/v1/u:chaos
[2]: http://feeds.pinboard.in/json/v1/u:chaos/t:Apple/
[3]: http://127.0.0.1:5000
[pinboard]: http://www.pinboard.in "Pinboard Bookmarks"