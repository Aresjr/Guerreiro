from sqlalchemy import func, ForeignKey

from app import db


class Setor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128))
    empresa = db.Column(db.Integer, ForeignKey('empresa.id'))
    dataCriacao = db.Column(db.Date, default=func.now())
    del_ = db.Column(key='del', type=db.Boolean, default=False)
