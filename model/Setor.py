from sqlalchemy import ForeignKey

from app import db


class Setor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128))
    empresa = db.Column(db.Integer, ForeignKey('empresa.id'))
    setorPai = db.Column(db.Integer, ForeignKey('setor.id'))
    del_ = db.Column(db.Boolean, key='del', default=False)
