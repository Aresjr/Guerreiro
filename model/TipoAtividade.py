from app import db
from model.Habilidade import Habilidade
from model.manyToMany.HabilidadeTipoAtividade import HabilidadeTipoAtividade


class TipoAtividade(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    habilidades = db.relationship(Habilidade, secondary=HabilidadeTipoAtividade, lazy=False)
    descricao = db.Column(db.String(128))
    del_ = db.Column(db.Boolean, default=False)
