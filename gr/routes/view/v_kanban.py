from app import app
from flask import render_template
from flask_login import login_required
from gr.service.UsuarioService import usuario_service


@app.route('/view/kanban')
@login_required
def v_kanban():
    return render_template('pages/kanban.html', usuarios=usuario_service.get_all())
