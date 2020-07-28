from sqlalchemy import func, ForeignKey
from app import db


class NivelAcesso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(128))
    criaUsuario = db.Column(db.Boolean, default=False)
    criaAtividades = db.Column(db.Boolean, default=False)
    usuarioCriacao = db.Column(db.Integer, ForeignKey('usuario.id'))
    dataCriacao = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, key='del', default=False)
