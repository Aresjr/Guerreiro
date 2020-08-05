from app import db


class Medalha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    icone = db.Column(db.String(255))
    del_ = db.Column(db.Boolean, default=False)
