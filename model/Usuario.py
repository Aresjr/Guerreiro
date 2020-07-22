from sqlalchemy import func, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # PESSOAL
    nome = db.Column(db.String(255))
    email = db.Column(db.String(128), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)

    # PERSONAGEM
    nickname = db.Column(db.String(20), unique=True, nullable=False)
    level = db.Column(db.Integer, default=1, nullable=False)
    currentXp = db.Column(db.Integer, default=0)
    nextLevelXp = db.Column(db.Integer, default=1000)

    # FKs
    group = db.Column(db.Integer, ForeignKey('grupo.id'))
    lang = db.Column(db.Integer, ForeignKey('lang.id'))
    raca = db.Column(db.Integer, ForeignKey('raca.id'))

    # PREFS
    darkMode = db.Column(db.Boolean, default=False)

    # VERSIONAMENTO
    dataCriacao = db.Column(db.Date, default=func.now())
    datAlteracao = db.Column(db.Date)
    del_ = db.Column(db.Boolean, default=False)

    def set_password(self, senha):
        self.senha = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.senha, senha)
