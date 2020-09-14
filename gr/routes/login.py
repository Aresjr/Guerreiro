from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import current_user
from gr.form.forms import LoginForm
from gr.service.LoginService import login_service
from gr.service.UsuarioService import usuario_service


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if login_service.verificar_login(form):
        return login_service.loga_usuario(form)
    return render_template('layouts/login.html', title="Login", form=form)


@app.route("/logout", methods=['GET'])
def logout():
    usuario_service.logout(current_user)
    flash('Você saiu do sistema', 'info')
    return redirect(url_for('login'))

