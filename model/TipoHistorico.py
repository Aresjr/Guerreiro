from sqlalchemy import func
from app import db


class TipoHistorico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(255), nullable=False)
    dataCriacao = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, key='del', default=False)
