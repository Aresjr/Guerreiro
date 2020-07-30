from app import db


class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(255))
    descricao = db.Column(db.String(255))
    del_ = db.Column(db.Boolean, key='del', default=False)
