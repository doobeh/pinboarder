from flask.ext.wtf import Form, TextField, PasswordField, TextAreaField
from flask.ext.wtf import Required, Email

class LoginForm(Form):
    email = TextField('Email address', [Required(), Email()])
    password = PasswordField('Password', [Required()])

class EditForm(Form):
    title = TextField('Post Title',[Required()])
    url = TextField('URL',[Required()])
    content = TextAreaField('Content (Markdown)')