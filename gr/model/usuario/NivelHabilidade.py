from app import db
from gr.model.usuario.Habilidade import Habilidade
from gr.model.usuario.Usuario import Usuario


class NivelHabilidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habilidade = db.relationship(Habilidade)
    level = db.Column(db.Integer, default=1)
    currentXp = db.Column(db.Integer, default=0)
    nextLevelXp = db.Column(db.Integer, default=100)

    usuarioId = db.Column(db.Integer, db.ForeignKey(Usuario.id))
    habilidadeId = db.Column(db.Integer, db.ForeignKey(Habilidade.id))
    del_ = db.Column(db.Boolean, default=False)
