from sqlalchemy import ForeignKey
from app import db
from model.Atividade import Atividade
from model.Usuario import Usuario


class AtividadeUsuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atividade_id = db.Column(db.Integer, ForeignKey(Atividade.id), nullable=False)
    usuario_id = db.Column(db.Integer, ForeignKey(Usuario.id), nullable=False)
    inicioAtividade = db.Column(db.Date)
    fimAtividade = db.Column(db.Date)
    totalMinutos = db.Column(db.Float)
    del_ = db.Column(db.Boolean, key='del', default=False)
