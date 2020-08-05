from app import db


class TipoConquista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(128), nullable=False)
    destaque = db.Column(db.Boolean, default=False)
    del_ = db.Column(db.Boolean, default=False)
