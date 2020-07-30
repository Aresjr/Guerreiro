from sqlalchemy import ForeignKey
from app import db


class Vaga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aberta = db.Column(db.Boolean, default=True)
    descricao = db.Column(db.String(255), nullable=False)
    cargo = db.Column(db.Integer, ForeignKey('cargo.id'))
    del_ = db.Column(db.Boolean, key='del', default=False)
