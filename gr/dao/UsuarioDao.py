from app import db
from gr.dao.BaseDao import BaseDao
from gr.model.usuario.Usuario import Usuario

class UsuarioDao(BaseDao):
    def get_by_username(self, username):
        return self.model.query.filter(self.model.username == username).first()

    def get_by_empresa(self, empresaId):
        return self.model.query.filter(self.model.empresaId == empresaId).all()

    def update(self, usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario

    def delete(self, usuario):
        usuario.del_ = True
        db.session.add(usuario)
        return db.session.commit()

    def purge(self, usuario):
        db.session.delete(usuario)
        return db.session.commit()


usuario_dao = UsuarioDao(Usuario)
