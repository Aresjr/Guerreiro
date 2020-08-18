from app import app
from flask import render_template
from flask_login import login_required, current_user


@app.route('/sobre', methods=['GET'])
@login_required
def sobre():
    # TODO
    usuario = current_user
    return render_template('pages/sobre.html', title="Sobre", usuario=usuario)
