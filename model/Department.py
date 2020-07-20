from sqlalchemy import func, ForeignKey

from app import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    company = db.Column(db.Integer, ForeignKey('company.id'))
    creationDate = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, default=False)
