from app import db
from gr.model.atividades.Atividade import Atividade
from gr.model.usuario.Usuario import Usuario


class Apontamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuadioId = db.Column(db.Integer, db.ForeignKey(Usuario.id), nullable=False)
    atividadeId = db.Column(db.Integer, db.ForeignKey(Atividade.id), nullable=False)
    dataInicio = db.Column(db.Date)
    dataFim = db.Column(db.Date)
