from app import app
from flask import render_template
from flask_login import current_user

from gr.dao.AtividadeEstagioDao import atividade_estagio_dao


@app.route('/')
def index():
    usuario = current_user
    return render_template('pages/index.html', usuario=usuario)

@app.route('/teste')
def teste():
    usuario = current_user
    for ai in atividade_estagio_dao.get_all():
        print(type(ai))
        print(ai)
    return render_template('pages/index.html', usuario=usuario)
