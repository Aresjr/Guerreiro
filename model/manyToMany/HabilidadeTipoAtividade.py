from sqlalchemy import ForeignKey
from app import db

HabilidadeTipoAtividade = db.Table('tipo_atividade_habilidade', db.metadata,
                                   db.Column('tipo_atividade_id', db.Integer, ForeignKey('tipo_atividade.id')),
                                   db.Column('habilidade_id', db.Integer, ForeignKey('habilidade.id')),
                                   db.Column('xp', db.Integer))
