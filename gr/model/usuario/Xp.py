from app import db
from gr.model.atividades.Atividade import Atividade
from gr.model.usuario.Habilidade import Habilidade


class Xp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atividadeId = db.Column(db.Integer, db.ForeignKey(Atividade.id))
    habilidadeId = db.Column(db.Integer, db.ForeignKey(Habilidade.id))
    contabilizado = db.Column(db.Boolean, nullable=False, default=False)
    dataContabilizacao = db.Column(db.Date)
