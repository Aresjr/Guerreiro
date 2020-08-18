from app import db

# TODO - migrar essa tabela para cá
NivelHabilidade = db.Table('nivel_habilidade', db.metadata,
                           db.Column('usuario_id', db.Integer, db.ForeignKey('usuario.id')),
                           db.Column('habilidade_id', db.Integer, db.ForeignKey('habilidade.id')),
                           db.Column('level', db.Integer, default=1),
                           db.Column('currentXp', db.Integer, default=0),
                           db.Column('nextLevelXp', db.Integer, default=100))
