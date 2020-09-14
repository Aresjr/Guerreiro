from app import app
from flask import render_template
from flask_login import login_required, current_user


@app.route('/view/conquistas')
@login_required
def v_conquistas():
    usuario = current_user
    return render_template('pages/conquistas.html', usuario=usuario)
