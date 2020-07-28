from sqlalchemy import func, ForeignKey
from app import db


class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer)
    desc = db.Column(db.String(255))
    inicioAtividade = db.Column(db.Date)
    fimAtividade = db.Column(db.Date)
    totalMinutos = db.Column(db.Float)
    usuarioCriacao = db.Column(db.Integer, ForeignKey('usuario.id'))
    dataCriacao = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, key='del', default=False)
