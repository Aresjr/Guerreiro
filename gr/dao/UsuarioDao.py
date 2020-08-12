from gr.model.usuario.Usuario import Usuario

class UsuarioDao:
    def __init__(self, model):
        self.model = model

    def get_by_username(self, username):
        return self.model.query.filter(self.model.username == username).first()


usuario_dao = UsuarioDao(Usuario)
