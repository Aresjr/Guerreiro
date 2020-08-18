from app import db


class Habilidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), unique=True)
    habPai = db.relationship('Habilidade')
    habPaiId = db.Column(db.ForeignKey(id))
    del_ = db.Column(db.Boolean, default=False)
