from app import app, db
from flask import render_template, redirect, url_for
from flask_login import login_user, current_user, logout_user
from gr.forms.forms import LoginForm
from gr.model.usuario.Usuario import Usuario


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter(Usuario.username == form.username.data.lower()).first()
        if usuario:
            if usuario.check_password(form.password.data):
                usuario.authenticated = True
                db.session.add(usuario)
                db.session.commit()
                login_user(usuario, remember=True)
                return redirect(form.next.data or url_for('index'))
    return render_template('layouts/login.html', title="Login", form=form)


@app.route("/logout", methods=['GET'])
def logout():
    usuario = current_user
    if usuario:
        usuario.authenticated = False
        db.session.add(usuario)
        db.session.commit()
        logout_user()
    return redirect(url_for('login'))

