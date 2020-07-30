from sqlalchemy import ForeignKey
from app import db


class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    nomeFantasia = db.Column(db.String(255))
    lang = db.Column(db.Integer, ForeignKey('lang.id'))
    xpConfigFator = db.Column(db.Float, default=1.15)
    xpConfigValorBase = db.Column(db.Integer, default=1000)
    del_ = db.Column(db.Boolean, key='del', default=False)
