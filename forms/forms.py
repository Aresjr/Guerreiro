from flask_wtf import Form
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
