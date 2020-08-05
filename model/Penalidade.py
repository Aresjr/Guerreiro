from app import db
from model.Atividade import Atividade
from model.Usuario import Usuario
from sqlalchemy import ForeignKey, func


class Penalidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255))
    atividade = db.relationship(Atividade, lazy=True)
    usuario = db.relationship(Usuario, lazy=True)
    dataPenalidade = db.Column(db.Date, default=func.now)
    atividadeId = db.Column(db.Integer, ForeignKey(Atividade.id), nullable=False)
    usuarioId = db.Column(db.Integer, ForeignKey(Usuario.id), nullable=False)
    del_ = db.Column(db.Boolean, default=False)
