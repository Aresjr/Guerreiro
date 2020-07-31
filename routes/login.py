from flask import render_template

from app import app


@app.route('/login', methods=['GET', 'POST'])
def login():
    # form = LoginForm()
    # if form.validate_on_submit():
    #     usuario = Usuario.query.get(form.email.data)
    #     if usuario:
    #         if bcrypt.check_password_hash(usuario.senha, form.senha.data):
    #             usuario.authenticated = True
    #             db.session.add(usuario)
    #             db.session.commit()
    #             login_user(usuario, remember=True)
    #             return redirect(url_for("/"))
    return render_template('layouts/login.html', title="Login")
