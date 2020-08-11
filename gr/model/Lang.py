from app import db


class Lang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(7), unique=True)
    descricao = db.Column(db.String(128), unique=True)