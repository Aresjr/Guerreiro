from app import db


class TipoItemLinhaTempo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(128), nullable=False)
    destaque = db.Column(db.Boolean, default=False)
    del_ = db.Column(db.Boolean, key='del', default=False)
