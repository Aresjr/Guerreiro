from sqlalchemy import ForeignKey
from app import db

AtividadeHabilidade = db.Table('atividade_habilidade', db.metadata,
                               db.Column('atividade_id', db.Integer, ForeignKey('atividade.id')),
                               db.Column('habilidade_id', db.Integer, ForeignKey('habilidade.id')),
                               db.Column('xp', db.Integer, nullable=False))
