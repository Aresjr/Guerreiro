from app import app, db
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user

from gr.dao.UsuarioDao import usuario_dao
from gr.form.forms import LoginForm
from gr.service.UsuarioService import usuario_service


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data.lower()
        login = usuario_service.verify_login(username, form.password.data)
        if login:
            usuario_service.login(username)
            return redirect(form.next.data or url_for('index'))
    return render_template('layouts/login.html', title="Login", form=form)


@app.route("/logout", methods=['GET'])
def logout():
    usuario_service.logout(current_user)
    flash('Você saiu do sistema', 'info')
    return redirect(url_for('login'))

