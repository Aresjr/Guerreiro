from app import db
from model.Atividade import Atividade
from model.Usuario import Usuario
from sqlalchemy import ForeignKey, func


class Execucao(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.Integer, ForeignKey(Usuario.id), nullable=False)
    atividade = db.relationship(Atividade, lazy=True)
    dataInicio = db.Column(db.Date, nullable=False, default=func.now)
    dataFim = db.Column(db.Date)

    atividadeId = db.Column(db.Integer, ForeignKey(Atividade.id), nullable=False)
