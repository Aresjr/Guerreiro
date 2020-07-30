from sqlalchemy import ForeignKey
from app import db


class AtividadeUsuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atividade = db.Column(db.Integer, ForeignKey('atividade.id'), nullable=False)
    usuario = db.Column(db.Integer, ForeignKey('usuario.id'), nullable=False)
    inicioAtividade = db.Column(db.Date)
    fimAtividade = db.Column(db.Date)
    totalMinutos = db.Column(db.Float)
    del_ = db.Column(db.Boolean, key='del', default=False)
