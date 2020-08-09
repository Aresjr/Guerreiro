from app import db


class NivelAcesso(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(128))

    # FUNCIONÁRIO
    fazAtividades = db.Column(db.Boolean, default=True)
    fazTeste = db.Column(db.Boolean, default=False)

    # ADM
    criaCargo = db.Column(db.Boolean, default=False)
    criaUsuario = db.Column(db.Boolean, default=False)

    # ANALISTA
    criaPenalidade = db.Column(db.Boolean, default=False)

    # RH / ADM
    criaAtividades = db.Column(db.Boolean, default=False)
    criaVaga = db.Column(db.Boolean, default=False)

    del_ = db.Column(db.Boolean, default=False)
