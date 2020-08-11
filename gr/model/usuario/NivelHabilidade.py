from app import db
from gr.model.usuario.Habilidade import Habilidade


class NivelHabilidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habilidade = db.relationship(Habilidade, lazy=True)
    level = db.Column(db.Integer, default=1)
    currentXp = db.Column(db.Integer, default=0)
    nextLevelXp = db.Column(db.Integer, default=10)

    usuarioId = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    habilidadeId = db.Column(db.Integer, db.ForeignKey(Habilidade.id))
    del_ = db.Column(db.Boolean, default=False)
