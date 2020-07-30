from sqlalchemy import ForeignKey
from app import db


class Habilidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    descricao = db.Column(db.String(128))
    habilidadePai = db.Column(db.Integer, ForeignKey('habilidade.id'))
    del_ = db.Column(db.Boolean, key='del', default=False)
