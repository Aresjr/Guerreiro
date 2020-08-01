from sqlalchemy import ForeignKey
from app import db
from model.Atividade import Atividade
from model.Habilidade import Habilidade


class Xp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    totalXp = db.Column(db.Integer)
    atividade = db.Column(db.Integer, ForeignKey(Atividade.id))
    habilidade = db.Column(db.Integer, ForeignKey(Habilidade.id))
    contabilizado = db.Column(db.Boolean, default=False)
