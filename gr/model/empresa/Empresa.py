from app import db


class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    nomeFantasia = db.Column(db.String(255))

    # CONFIG
    xpFator = db.Column(db.Float, default=0.15)
    xpPrimeiroNivel = db.Column(db.Integer, default=100)
    xpPorAtividade = db.Column(db.Integer, default=12)
    hpInicial = db.Column(db.Integer, default=1000)
    nivelHpUp = db.Column(db.Integer, default=10)
    penalidadeConfigHpDown = db.Column(db.Integer, default=10)
    enviaDadosAnonimos = db.Column(db.Boolean)

    del_ = db.Column(db.Boolean, default=False)
