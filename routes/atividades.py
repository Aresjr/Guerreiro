from app import app
from flask import render_template
from flask_login import login_required, current_user


@app.route('/atividades', methods=['GET'])
@login_required
def atividades():
    usuario = current_user
    qt_atividade_linha = 4
    return render_template('pages/atividades.html', title="Atividades", usuario=usuario,
                           qt_atividade_linha=qt_atividade_linha)
