from app import db


class Habilidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), unique=True)
    habPai = db.Column(db.ForeignKey(id))
    del_ = db.Column(db.Boolean, default=False)
