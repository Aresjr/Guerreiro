from app import app
from flask import render_template, abort
from flask_login import current_user
from gr.service.UsuarioService import usuario_service


@app.route('/view/kanban')
def v_kanban():
    usuario = current_user
    print(usuario)
    if usuario is None:
        return abort(401)
    return render_template('pages/kanban.html', usuarios=usuario_service.get_all())
