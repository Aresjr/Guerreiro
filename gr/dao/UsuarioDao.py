from app import db
from gr.model.usuario.Usuario import Usuario

class UsuarioDao:
    def __init__(self, model):
        self.model = model

    def get_by_id(self, usuario_id):
        return self.model.query.get(usuario_id).first()

    def get_by_username(self, username):
        return self.model.query.filter(self.model.username == username).first()

    def update(self, usuario):
        db.session.add(usuario)
        return db.session.commit()


usuario_dao = UsuarioDao(Usuario)
