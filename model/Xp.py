from sqlalchemy import ForeignKey
from app import db


class Xp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    totalXp = db.Column(db.Integer)
    atividade = db.Column(db.Integer, ForeignKey('atividade.id'))
    habilidade = db.Column(db.Integer, ForeignKey('habilidade.id'))
