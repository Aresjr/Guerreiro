from sqlalchemy import ForeignKey
from app import db
from model.Cargo import Cargo
from model.Habilidade import Habilidade


class RequisitoCargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String, nullable=False)
    cargo = db.Column(db.Integer, ForeignKey(Cargo.id), nullable=False)
    habilidade = db.Column(db.Integer, ForeignKey(Habilidade.id), nullable=False)
    nivelMinimo = db.Column(db.Integer, nullable=False)
    del_ = db.Column(db.Boolean, key='del', default=False)
