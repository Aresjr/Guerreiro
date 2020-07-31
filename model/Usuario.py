from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nivelAcesso = db.Column(db.Integer, ForeignKey('nivel_acesso.id'))

    # FUNCIONÁRIO
    setor = db.Column(db.Integer, ForeignKey('setor.id'))
    cargo = db.Column(db.Integer, ForeignKey('cargo.id'))
    cargoDesejado = db.Column(db.Integer, ForeignKey('cargo.id'))

    # PESSOAL
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)

    # PERSONAGEM
    nickname = db.Column(db.String(20), unique=True, nullable=False)
    level = db.Column(db.Integer, default=1, nullable=False)
    currentXp = db.Column(db.Integer, default=0)
    nextLevelXp = db.Column(db.Integer, default=1000)

    # PREFS
    darkMode = db.Column(db.Boolean, default=False)
    lang = db.Column(db.Integer, ForeignKey('lang.id'))

    authenticated = db.Column(db.Boolean, default=False)
    del_ = db.Column(db.Boolean, key='del', default=False)

    def set_password(self, senha):
        self.senha = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.senha, senha)

    def is_active(self):
        return not self.del_

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    @login_manager.user_loader
    def user_loader(id):
        return Usuario.query.get(id)
