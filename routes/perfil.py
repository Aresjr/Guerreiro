from app import app
from flask import render_template
from flask_login import login_required, current_user


@app.route('/perfil')
@login_required
def perfil():
    usuario = current_user
    return render_template('pages/perfil.html', title="Perfil", usuario=usuario)
