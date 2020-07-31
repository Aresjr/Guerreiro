from sqlalchemy import ForeignKey
from app import db


class Conquista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    tipoItem = db.Column(db.Integer, ForeignKey('tipo_conquista.id'))
    del_ = db.Column(db.Boolean, key='del', default=False)
