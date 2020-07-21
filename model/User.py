from sqlalchemy import func, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model):
    __tablename__ = 'user_'
    id = db.Column(db.Integer, primary_key=True)

    # PERSONAL
    name = db.Column(db.String(255))
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    # CHARACTER
    nickname = db.Column(db.String(20), unique=True, nullable=False)
    level = db.Column(db.Integer, default=1, nullable=False)
    currentXp = db.Column(db.Integer, default=0)
    nextLevelXp = db.Column(db.Integer, default=1000)

    # FKs
    role = db.Column(db.Integer, ForeignKey('role.id'), nullable=False)
    group = db.Column(db.Integer, ForeignKey('group_.id'))
    lang = db.Column(db.Integer, ForeignKey('lang.id'))
    race = db.Column(db.Integer, ForeignKey('race.id'))

    # PREFS
    darkMode = db.Column(db.Boolean, default=False)

    # VERSIONING
    creationDate = db.Column(db.Date, default=func.now())
    alterDate = db.Column(db.Date)
    del_ = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
