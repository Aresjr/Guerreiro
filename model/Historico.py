from sqlalchemy import func, ForeignKey
from app import db


class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(255), nullable=False)
    tipoHistorico = db.Column(db.Integer, ForeignKey('tipo_historico.id'))
    usuarioCriacao = db.Column(db.Integer, ForeignKey('usuario.id'))
    dataCriacao = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, key='del', default=False)
