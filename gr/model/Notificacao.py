from app import db
from gr.model.Usuario import Usuario


class Notificacao(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    tipoNotificacaoId = db.Column(db.Integer, nullable=False)
    titulo = db.Column(db.String(128))
    descricao = db.Column(db.String(255))
    lida = db.Column(db.Boolean, default=False)
    usuarioCriacao = db.Column(db.ForeignKey(Usuario.id))
    usuarioLeitura = db.Column(db.ForeignKey(Usuario.id))
    dataCriacao = db.Column(db.Date, default=db.func.now())
    dataLeitura = db.Column(db.Date)
