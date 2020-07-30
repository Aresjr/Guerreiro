from sqlalchemy import ForeignKey, func
from app import db


class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tabela = db.Column(db.String(255), nullable=False)
    idTabela = db.Column(db.Integer, nullable=False)
    valorNovo = db.Column(db.String(255), nullable=False)
    valorAntigo = db.Column(db.String(255), nullable=False)
    usuarioAlteracao = db.Column(db.Integer, ForeignKey('usuario.id'))
    dataAlteracao = db.Column(db.Date, default=func.now())
