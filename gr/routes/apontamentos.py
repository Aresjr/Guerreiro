from app import app
from flask import render_template
from flask_login import login_required, current_user


@app.route('/apontamentos', methods=['GET'])
@login_required
def apontamentos():
    # TODO
    usuario = current_user
    return render_template('pages/apontamentos.html', title="Apontamentos", usuario=usuario)
