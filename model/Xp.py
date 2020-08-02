from sqlalchemy import ForeignKey, func
from app import db
from model.Atividade import Atividade
from model.Habilidade import Habilidade


class Xp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atividade = db.relationship(Atividade, lazy=False)
    dataCriacao = db.Column(db.Date, default=func.now)
    dataContabilizacao = db.Column(db.Date)

    atividadeId = db.Column(db.Integer, ForeignKey(Atividade.id))
    habilidadeId = db.Column(db.Integer, ForeignKey(Habilidade.id))
