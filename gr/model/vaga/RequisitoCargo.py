from app import db
from gr.model.vaga.Cargo import Cargo
from gr.model.usuario.Habilidade import Habilidade


class RequisitoCargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String, nullable=False)
    cargo = db.Column(db.Integer,db.ForeignKey(Cargo.id), nullable=False)
    habilidade = db.Column(db.Integer,db.ForeignKey(Habilidade.id), nullable=False)
    nivelMinimo = db.Column(db.Integer, nullable=False)
    del_ = db.Column(db.Boolean, default=False)
