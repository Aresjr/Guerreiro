from app import db

HabilidadeTipoAtividade = db.Table('tipo_atividade_habilidade', db.metadata,
                                   db.Column('tipo_atividade_id', db.Integer, db.ForeignKey('tipo_atividade.id')),
                                   db.Column('habilidade_id', db.Integer, db.ForeignKey('habilidade.id')))
