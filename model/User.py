from sqlalchemy import func, ForeignKey

from app import db


class User(db.Model):
    __tablename__ = 'user_'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(128), unique=True, nullable=False)
    nickname = db.Column(db.String(20), unique=True, nullable=False)
    group = db.Column(db.Integer, ForeignKey('group_.id'))
    level = db.Column(db.Integer, default=1, nullable=False)
    lang = db.Column(db.Integer, ForeignKey('lang.id'))
    darkMode = db.Column(db.Boolean, default=False)
    creationDate = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, default=False)
