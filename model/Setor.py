from sqlalchemy import func, ForeignKey

from app import db


class Setor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128))
    empresa = db.Column(db.Integer, ForeignKey('empresa.id'))
    setor = db.Column(db.Integer, ForeignKey('setor.id'))
    usuarioCriacao = db.Column(db.Integer, ForeignKey('usuario.id'))
    dataCriacao = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, key='del', default=False)
