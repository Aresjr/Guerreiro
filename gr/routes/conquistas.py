from app import app
from flask import render_template
from flask_login import login_required, current_user


@app.route('/conquistas', methods=['GET'])
@login_required
def conquistas():
    usuario = current_user
    return render_template('pages/conquistas.html', title="Conquistas", usuario=usuario)