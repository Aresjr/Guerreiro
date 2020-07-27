from sqlalchemy import func, ForeignKey
from app import db


class Xp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    totalXp = db.Column(db.Integer)
    tarefa = db.Column(db.Integer, ForeignKey('tarefa.id'))
    habilidade = db.Column(db.Integer, ForeignKey('habilidade.id'))
    usuarioCriacao = db.Column(db.Integer, ForeignKey('usuario.id'))
    dataCriacao = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, key='del', default=False)
