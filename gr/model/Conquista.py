from app import db
from gr.model.TipoConquista import TipoConquista
from gr.model.Usuario import Usuario


class Conquista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    tipoItem = db.Column(db.Integer, db.ForeignKey(TipoConquista.id))
    usuadioId = db.Column(db.Integer, db.ForeignKey(Usuario.id))
