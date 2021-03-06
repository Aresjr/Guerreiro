from app import db

AtividadeEstagio = db.Table('atividade_estagio', db.metadata,
                            db.Column('atividade_id', db.Integer, db.ForeignKey('atividade.id')),
                            db.Column('estagio_id', db.Integer, db.ForeignKey('estagio.id')),
                            db.Column('usuario_id', db.Integer, db.ForeignKey('usuario.id')),
                            db.Column('incio_atividade', db.Date),
                            db.Column('fim_atividade', db.Date))
