from sqlalchemy import func
from app import db


class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer)
    desc = db.Column(db.String(255))
    inicioAtividade = db.Column(db.Date)
    fimAtividade = db.Column(db.Date)
    totalMinutos = db.Column(db.Float)
    dataCriacao = db.Column(db.Date, default=func.now())
    del_ = db.Column(key='del', type=db.Boolean, default=False)
