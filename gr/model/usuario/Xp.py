from app import db
from gr.model.atividades.Atividade import Atividade
from gr.model.usuario.Habilidade import Habilidade


class Xp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atividade = db.relationship(Atividade, lazy=False)
    dataCriacao = db.Column(db.Date, default=db.func.now)
    dataContabilizacao = db.Column(db.Date)

    atividadeId = db.Column(db.Integer,db.ForeignKey(Atividade.id))
    habilidadeId = db.Column(db.Integer,db.ForeignKey(Habilidade.id))
