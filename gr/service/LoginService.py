from flask import url_for, flash
from gr.service.UsuarioService import usuario_service
from werkzeug.utils import redirect


class LoginService:

    def verificar_login(self, form):
        if form.validate_on_submit():
            username = form.username.data.lower()
            login = usuario_service.verify_login(username, form.password.data)
            if not login:
                flash('Usuário e/ou senha inválidos', 'danger')
            return login

    def loga_usuario(self, form):
        username = form.username.data.lower()
        remember_me = form.remember_me.data
        usuario_service.login(username, remember_me)
        return redirect(form.next.data or url_for('index'))


login_service = LoginService()
