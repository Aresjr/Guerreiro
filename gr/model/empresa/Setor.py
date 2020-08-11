from app import db
from gr.model.empresa.Empresa import Empresa


class Setor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128))
    empresa = db.relationship(Empresa, lazy=True)

    setorPaiId = db.Column(db.ForeignKey('setor.id'))
    empresaId = db.Column(db.ForeignKey(Empresa.id))
    del_ = db.Column(db.Boolean, default=False)
