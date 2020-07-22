from sqlalchemy import func, ForeignKey
from app import db


class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128))
    fantasynome = db.Column(db.String(255))
    lang = db.Column(db.Integer, ForeignKey('lang.id'))
    dataCriacao = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, default=False)
