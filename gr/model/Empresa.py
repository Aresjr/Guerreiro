from app import db
from gr.model.Lang import Lang


class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    nomeFantasia = db.Column(db.String(255))
    lang = db.Column(db.Integer, db.ForeignKey(Lang.id))

    # CONFIG
    xpConfigFator = db.Column(db.Float, default=1.15)
    xpConfigValorBase = db.Column(db.Integer, default=100)
    hpCondigInicial = db.Column(db.Integer, default=1000)
    nivelConfigHpUp = db.Column(db.Integer, default=100)
    penalidadeConfigHpDown = db.Column(db.Integer, default=100)

    del_ = db.Column(db.Boolean, default=False)
