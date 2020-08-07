from app import db

AtividadeHabilidade = db.Table('atividade_habilidade', db.metadata,
                               db.Column('atividade_id', db.Integer, db.ForeignKey('atividade.id')),
                               db.Column('habilidade_id', db.Integer, db.ForeignKey('habilidade.id')),
                               db.Column('xp', db.Integer))
