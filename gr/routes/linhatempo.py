from app import app
from flask import render_template
from flask_login import login_required, current_user


@app.route('/linhatempo', methods=['GET'])
@login_required
def linhatempo():
    usuario = current_user
    return render_template('pages/atividades.html', title="Atividades", usuario=usuario)
