from app import db
from gr.model.usuario.TipoConquista import TipoConquista
from gr.model.usuario.Usuario import Usuario


class Conquista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.relationship(TipoConquista, lazy=True)
    tipoId = db.Column(db.ForeignKey(TipoConquista.id), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    usuarioId = db.Column(db.Integer, db.ForeignKey(Usuario.id))
