from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    email = TextField('email', validators=[DataRequired()])
    password = PasswordField('senha', validators=[DataRequired()])
