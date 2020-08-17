from flask_login import login_user, logout_user

from gr.dao.UsuarioDao import usuario_dao


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
        usuario_dao.update(usuario)
        login_user(usuario, remember=True)
        return usuario

    def logout(self, usuario):
        if usuario:
            usuario.authenticated = False
            usuario_dao.update(usuario)
            logout_user()

    def add_xp(self, usuario, total_xp):
        xp_fator = usuario.setor.empresa.xpFator
        while usuario.currentXp + total_xp > usuario.nextLevelXp:
            usuario.level += 1
            total_xp -= usuario.nextLevelXp
            usuario.nextLevelXp = round(usuario.nextLevelXp * xp_fator)
        usuario.currentXp += total_xp  # total_xp que sobra
        return usuario_dao.update(usuario)


usuario_service = UsuarioService()
