from app import db
from model.TipoAtividade import TipoAtividade
from sqlalchemy import ForeignKey

from model.Usuario import Usuario


class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(255))
    tipoAtividade = db.relationship(TipoAtividade, lazy=True)
    # usuario = db.relationship(Usuario, lazy=True)
    descricao = db.Column(db.String(255))
    prioridade = db.Column(db.Integer)
    xpContabilizado = db.Column(db.Boolean, default=False, nullable=False)
    atividadePaiId = db.Column(db.Integer)

    usuarioId = db.Column(db.Integer)
    tipoAtividadeId = db.Column(db.Integer, ForeignKey(TipoAtividade.id))
    del_ = db.Column(db.Boolean, default=False)
