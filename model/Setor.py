from sqlalchemy import ForeignKey

from app import db
from model.Empresa import Empresa


class Setor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128))
    empresa = db.Column(db.Integer, ForeignKey(Empresa.id))
    setorPai = db.Column(db.Integer, ForeignKey('setor.id'))
    del_ = db.Column(db.Boolean, default=False)
