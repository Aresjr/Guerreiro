from sqlalchemy import func

from app import db


class Lang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(7), unique=True)
    description = db.Column(db.String(128), unique=True)
    creationDate = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, default=False)
