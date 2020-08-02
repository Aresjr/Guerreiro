from sqlalchemy import ForeignKey, func

from app import db
from model.Atividade import Atividade


class Penalidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255))
    atividade = db.Column(db.Integer, ForeignKey(Atividade.id))
    dataPenalidade = db.Column(db.Date, default=func.now)
    del_ = db.Column(db.Boolean, key='del', default=False)
