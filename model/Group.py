from sqlalchemy import func, ForeignKey

from app import db


class Group(db.Model):
    __tablename__ = 'group_'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    department = db.Column(db.Integer, ForeignKey('department.id'))
    creationDate = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, default=False)
