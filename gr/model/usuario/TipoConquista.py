from app import db


class TipoConquista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128), nullable=False)
    destaque = db.Column(db.Boolean, default=False)
    icone = db.Column(db.String(128), default=False)
    del_ = db.Column(db.Boolean, default=False)
