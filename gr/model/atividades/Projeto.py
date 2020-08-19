from app import db


class Projeto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    del_ = db.Column(db.Boolean, default=False)
