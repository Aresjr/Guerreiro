from sqlalchemy import ForeignKey
from app import db

NivelHabilidadeUsuario = db.Table('nivel_habilidade_usuario', db.metadata,
                                  db.Column('nivel_habilidade_id', db.Integer, ForeignKey('nivel_habilidade.id')),
                                  db.Column('usuario_id', db.Integer, ForeignKey('usuario.id')))
