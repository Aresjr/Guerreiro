from app import db


class Cargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    cargoSuperior = db.Column(db.Integer, db.ForeignKey(id))
    del_ = db.Column(db.Boolean, default=False)
