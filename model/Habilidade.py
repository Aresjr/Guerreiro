from sqlalchemy import func, ForeignKey
from app import db


class Habilidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(128))
    habilidadePai = db.Column(db.Integer, ForeignKey('habilidade.id'))
    dataCriacao = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, key='del', default=False)
