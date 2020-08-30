from app import db
from gr.model.empresa.Empresa import Empresa


class Estagio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128), unique=True)
    atividades = db.relationship('Atividade')
    empresa = db.relationship('Empresa')
    estagioInicial = db.Column(db.Boolean, default=False)
    estagioTeste = db.Column(db.Boolean, default=False)
    estagioFinal = db.Column(db.Boolean, default=False)
    ordem = db.Column(db.Integer)
    empresaId = db.Column(db.ForeignKey(Empresa.id))
    del_ = db.Column(db.Boolean, default=False)
