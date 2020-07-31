from app import app, db
from flask import render_template, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from forms.forms import LoginForm
from model.Usuario import Usuario


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
                return redirect(url_for('perfil'))

    return render_template('layouts/login.html', title="Login", form=form)


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    usuario = current_user
    usuario.authenticated = False
    db.session.add(usuario)
    db.session.commit()
    logout_user()
    return render_template("pages/logout.html")
