from sqlalchemy import ForeignKey

from app import db
from model.Atividade import Atividade
from model.Habilidade import Habilidade


class AtividadeHabilidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atividadeId = db.Column(db.Integer, ForeignKey(Atividade), nullable=False)
    habilidadeId = db.Column(db.Integer, ForeignKey(Habilidade), nullable=False)
    xp = db.Column(db.Integer, nullable=False)
