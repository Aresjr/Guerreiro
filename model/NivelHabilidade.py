from app import db
from model.Habilidade import Habilidade
from model.Usuario import Usuario
from sqlalchemy import ForeignKey


class NivelHabilidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.relationship(Usuario, lazy=True)
    habilidade = db.relationship(Habilidade, lazy=True)
    level = db.Column(db.Integer, default=1)
    currentXp = db.Column(db.Integer, default=0)
    nextLevelXp = db.Column(db.Integer, default=10)

    # FKs
    usuarioId = db.Column(db.Integer, ForeignKey(Usuario.id))
    habilidadeId = db.Column(db.Integer, ForeignKey(Habilidade.id))
    del_ = db.Column(db.Boolean, key='del', default=False)
