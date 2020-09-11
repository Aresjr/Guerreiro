from flask_login import login_user, logout_user
from gr.dao.ConquistaDao import conquista_dao
from gr.dao.TipoConquistaDao import tipo_conquista_dao
from gr.dao.UsuarioDao import usuario_dao
from gr.model.usuario.Conquista import Conquista


class UsuarioService:

    def verify_login(self, username, password):
        usuario = usuario_dao.get_by_username(username)
        if usuario:
            if usuario.check_password(password):
                return True
        return False

    def login(self, username):
        usuario = usuario_dao.get_by_username(username)
        usuario.authenticated = True
        usuario_dao.upsert(usuario)
        login_user(usuario, remember=True)
        return usuario

    def logout(self, usuario):
        if usuario:
            usuario.authenticated = False
            usuario_dao.upsert(usuario)
            logout_user()

    def add_xp(self, usuario, total_xp):
        leveled_up = False
        xp_fator = usuario.setor.empresa.xpFator
        conquista_level_up = tipo_conquista_dao.get_by_titulo('Level Up!')
        while usuario.currentXp + total_xp >= usuario.nextLevelXp:
            usuario.level += 1
            total_xp -= usuario.nextLevelXp
            usuario.nextLevelXp = round(usuario.nextLevelXp * xp_fator)
            if conquista_level_up:
                conquista_dao.upsert(Conquista(usuarioId=usuario.id, tipoId=conquista_level_up.id, descricao=conquista_level_up.descricao.format(str(usuario.level))))
            leveled_up = True
        usuario.currentXp += total_xp  # total_xp que sobra
        return usuario_dao.upsert(usuario)

    def get_usuarios_empresa(self, empresaId):
        usuarios = usuario_dao.get_by_empresa(empresaId)
        usuarios_json = []
        for usuario in usuarios:
            usuarios_json.append({
                'label': usuario.nome,
                'id': usuario.id
            })
        return usuarios_json

    def get_all(self):
        return usuario_dao.get_all()


usuario_service = UsuarioService()
