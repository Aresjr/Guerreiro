from sqlalchemy import func, ForeignKey
from app import db


class Lang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(7), unique=True)
    desc = db.Column(db.String(128), unique=True)
    usuarioCriacao = db.Column(db.Integer, ForeignKey('usuario.id'))
    dataCriacao = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, key='del', default=False)
