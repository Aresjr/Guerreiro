from app import db


class NivelAcesso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    criaUsuario = db.Column(db.Boolean, default=False)
    criaAtividades = db.Column(db.Boolean, default=False)
    criaCargo = db.Column(db.Boolean, default=False)
    criaVaga = db.Column(db.Boolean, default=False)
    del_ = db.Column(db.Boolean, key='del', default=False)
