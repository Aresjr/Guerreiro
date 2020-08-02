from sqlalchemy import ForeignKey
from app import db

AtividadeUsuario = db.Table('atividade_usuario', db.metadata,
                            db.Column('atividade_id', db.Integer, ForeignKey('atividade.id')),
                            db.Column('usuario_id', db.Integer, ForeignKey('usuario.id')))
