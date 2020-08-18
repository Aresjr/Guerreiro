from app import app
from flask import render_template
from flask_login import login_required, current_user


@app.route('/quadro', methods=['GET'])
@login_required
def quadro():
    return render_template('pages/quadros.html', title="Quadro de Atividades", usuario=current_user)
