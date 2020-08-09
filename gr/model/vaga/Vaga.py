from app import db
from gr.model.vaga.Cargo import Cargo


class Vaga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aberta = db.Column(db.Boolean, default=True)
    descricao = db.Column(db.String(255), nullable=False)
    cargo = db.Column(db.Integer,db.ForeignKey(Cargo.id))
    del_ = db.Column(db.Boolean, default=False)
