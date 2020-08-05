from app import db


class Estagio(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    estagioTeste = db.Column(db.Boolean, default=False)
    estagioFinal = db.Column(db.Boolean, default=False)
    dataVigenciaInicio = db.Column(db.Date)
    dataVigenciaFim = db.Column(db.Date)

    del_ = db.Column(db.Boolean, default=False)
