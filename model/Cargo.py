from sqlalchemy import func, ForeignKey
from app import db


class Cargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(255), nullable=False)
    cargoSuperior = db.Column(db.Integer, ForeignKey('cargo.id'))
    cargoInicial = db.Column(db.Boolean, default=False)
    usuarioCriacao = db.Column(db.Integer, ForeignKey('usuario.id'))
    dataCriacao = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, key='del', default=False)
