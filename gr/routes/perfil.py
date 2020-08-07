from app import app
from flask import render_template
from flask_login import login_required, current_user


@app.route('/perfil', methods=['GET'])
@login_required
def perfil():
    return render_template('pages/perfil.html', title="Perfil", usuario=current_user)
