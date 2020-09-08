from app import app
from flask import render_template
from flask_login import login_required, current_user


@app.route('/view/perfil')
@login_required
def v_perfil():
    return render_template('pages/perfil.html', usuario=current_user)
