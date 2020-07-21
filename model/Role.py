from sqlalchemy import func
from app import db


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(128))
    creationDate = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, default=False)
