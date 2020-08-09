from app import app
from flask import render_template
from flask_login import login_required, current_user


@app.route('/mestre', methods=['GET'])
@login_required
def mestre():
    usuario = current_user
    return render_template('pages/mestre.html', title="Mestre", usuario=usuario)
