from app import db
from gr.model.usuario.Habilidade import Habilidade
from gr.model.manyToMany.HabilidadeTipoAtividade import HabilidadeTipoAtividade


# TODO - utilizar para pré carregar as habilidades ao cadastrar uma atividade deste tipo
class TipoAtividade(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    habilidades = db.relationship(Habilidade, secondary=HabilidadeTipoAtividade, lazy=False)
    descricao = db.Column(db.String(128))
    del_ = db.Column(db.Boolean, default=False)
