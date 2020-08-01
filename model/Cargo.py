from sqlalchemy import ForeignKey
from app import db


class Cargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    cargoSuperior = db.Column(db.Integer, ForeignKey(id))
    cargoInicial = db.Column(db.Boolean, default=False)
    del_ = db.Column(db.Boolean, key='del', default=False)
