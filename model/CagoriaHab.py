from sqlalchemy import func
from app import db


class CategoriaHab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(128))
    dataCriacao = db.Column(db.Date, default=func.now())
    del_ = db.Column(db.Boolean, default=False)
