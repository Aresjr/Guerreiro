from sqlalchemy import ForeignKey
from app import db
from model.TipoConquista import TipoConquista


class Conquista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    tipoItem = db.Column(db.Integer, ForeignKey(TipoConquista.id))
    del_ = db.Column(db.Boolean, default=False)
