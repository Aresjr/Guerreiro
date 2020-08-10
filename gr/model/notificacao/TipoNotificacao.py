from app import db


class TipoNotificacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    icone = db.Column(db.String(128), default=False)
