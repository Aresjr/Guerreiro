from flask_wtf import Form
from wtforms import PasswordField, StringField, HiddenField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', id="customCheck")
    next = HiddenField('next')
