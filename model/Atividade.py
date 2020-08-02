from app import db
from model.Habilidade import Habilidade
from model.TipoAtividade import TipoAtividade
from model.manyToMany.AtividadeHabilidade import AtividadeHabilidade
from sqlalchemy import ForeignKey, func


class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(255))
    tipoAtividade = db.relationship(TipoAtividade, lazy=True)
    descricao = db.Column(db.String(255))
    dataInicio = db.Column(db.Date, default=func.now)
    dataFim = db.Column(db.Date)
    xpContabilizado = db.Column(db.Boolean, default=False, nullable=False)
    habilidades = db.relationship(Habilidade, secondary=AtividadeHabilidade, lazy=True)

    tipoAtividadeId = db.Column(db.Integer, ForeignKey(TipoAtividade.id))
    del_ = db.Column(db.Boolean, key='del', default=False)
