from flask import url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from app import db, login_manager
from gr.model.vaga.Cargo import Cargo
from gr.model.Lang import Lang
from gr.model.usuario.NivelAcesso import NivelAcesso
from gr.model.empresa.Setor import Setor


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nivelAcesso = db.relationship(NivelAcesso, lazy=True)

    setor = db.relationship(Setor, lazy=True)
    cargo = db.relationship(Cargo, lazy=True)

    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    username = db.Column(db.String(50), unique=True, nullable=False)
    level = db.Column(db.Integer, default=1)
    currentXp = db.Column(db.Integer, default=0)
    nextLevelXp = db.Column(db.Integer, default=100)
    hp = db.Column(db.Integer, default=100)

    darkMode = db.Column(db.Boolean, default=False)
    lang = db.relationship(Lang)

    langId = db.Column(db.ForeignKey(Lang.id))
    nivelAcessoId = db.Column(db.Integer, db.ForeignKey(NivelAcesso.id))
    setorId = db.Column(db.ForeignKey(Setor.id))
    cargoId = db.Column(db.ForeignKey(Cargo.id))

    authenticated = db.Column(db.Boolean, default=False)
    del_ = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_active(self):
        return not self.del_

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    @login_manager.user_loader
    def user_loader(user_id):
        return Usuario.query.get(user_id)

    @login_manager.unauthorized_handler
    def unauthorized():
        flash('Você deve realizar o login para acessar essa página', 'error')
        flash(request.url, 'next')
        return redirect(url_for('login'))

    def addXp(self, xp):
        return self
