from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from model.Cargo import Cargo
from model.Lang import Lang
from model.NivelAcesso import NivelAcesso
from model.Setor import Setor


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nivelAcesso = db.Column(db.Integer, ForeignKey(NivelAcesso.id))

    # FUNCIONÁRIO
    setor = db.Column(db.Integer, ForeignKey(Setor.id))
    cargo = db.Column(db.Integer, ForeignKey(Cargo.id))
    cargoDesejado = db.Column(db.Integer, ForeignKey(Cargo.id))

    # PESSOAL
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    # PERSONAGEM
    username = db.Column(db.String(20), unique=True, nullable=False)
    level = db.Column(db.Integer, default=1)
    currentXp = db.Column(db.Integer, default=0)
    nextLevelXp = db.Column(db.Integer, default=1000)

    # PREFS
    darkMode = db.Column(db.Boolean, default=False)
    lang = db.Column(db.Integer, ForeignKey(Lang.id))

    authenticated = db.Column(db.Boolean, default=False)
    del_ = db.Column(db.Boolean, key='del', default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_active(self):
        return not self.del_

    def get_id(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    @login_manager.user_loader
    def user_loader(username):
        return Usuario.query.filter(Usuario.username == username).first()
