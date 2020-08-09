from app import db
from gr.model.atividades.Atividade import Atividade
from gr.model.usuario.Usuario import Usuario


class Penalidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255))
    atividade = db.relationship(Atividade, lazy=True)
    usuario = db.relationship(Usuario, lazy=True)
    dataPenalidade = db.Column(db.Date, default=db.func.now)
    atividadeId = db.Column(db.Integer, db.ForeignKey(Atividade.id), nullable=False)
    usuarioId = db.Column(db.Integer, db.ForeignKey(Usuario.id), nullable=False)
    del_ = db.Column(db.Boolean, default=False)
