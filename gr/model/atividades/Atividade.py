from app import db
from gr.model.atividades.Estagio import Estagio
from gr.model.atividades.Projeto import Projeto
from gr.model.atividades.TipoAtividade import TipoAtividade
from gr.model.usuario.Usuario import Usuario


class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(255))
    tipoAtividade = db.relationship(TipoAtividade, lazy=True)
    estagio = db.relationship(Estagio, lazy=True)
    descricao = db.Column(db.String(255))
    prioridade = db.Column(db.Integer)
    usuarioExecucao = db.relationship(Usuario)
    xpContabilizado = db.Column(db.Boolean, default=False, nullable=False)
    dataContabilizacao = db.Column(db.Date)

    atividadePaiId = db.Column(db.ForeignKey(id))
    usuarioExecucaoId = db.Column(db.ForeignKey(Usuario.id))
    tipoAtividadeId = db.Column(db.ForeignKey(TipoAtividade.id))
    estagioId = db.Column(db.ForeignKey(Estagio.id))
    projetoId = db.Column(db.ForeignKey(Projeto.id))
    del_ = db.Column(db.Boolean, default=False)
