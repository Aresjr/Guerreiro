from app import db
from gr.model.TipoAtividade import TipoAtividade
from gr.model.Usuario import Usuario


class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(255))
    tipoAtividade = db.relationship(TipoAtividade, lazy=True)
    descricao = db.Column(db.String(255))
    prioridade = db.Column(db.Integer)
    xpContabilizado = db.Column(db.Boolean, default=False, nullable=False)
    atividadePaiId = db.Column(db.Integer)

    usuarioExecucao = db.Column(db.Integer, db.ForeignKey(Usuario.id))
    tipoAtividadeId = db.Column(db.Integer, db.ForeignKey(TipoAtividade.id))
    del_ = db.Column(db.Boolean, default=False)
