from sqlalchemy import func, ForeignKey
from app import db


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    fantasyName = db.Column(db.String(255))
    lang = db.Column(db.Integer, ForeignKey('lang.id'))
    creationDate = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, default=False)
