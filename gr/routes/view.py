from app import app
from flask import render_template, abort
from flask_login import current_user

from gr.dao.ConquistaDao import conquista_dao
from gr.service.NivelHabilidadeService import nivel_habilidade_service
from gr.service.UsuarioService import usuario_service


@app.route('/view/perfil')
def v_perfil():
    usuario = current_user
    if usuario.is_anonymous:
        return abort(401)
    return render_template('views/perfil.html', usuario=usuario, nhs=nivel_habilidade_service.get_nh_usuario(usuario.id), width=int(100 / usuario.nextLevelXp * usuario.currentXp))

@app.route('/view/kanban')
def v_kanban():
    usuario = current_user
    if usuario.is_anonymous:
        return abort(401)
    return render_template('views/kanban.html', usuarios=usuario_service.get_all())

@app.route('/view/conquistas')
def v_conquistas():
    usuario = current_user
    if usuario.is_anonymous:
        return abort(401)
    return render_template('views/conquistas.html', usuario=usuario, conquistas=conquista_dao.get_by_usuario(usuario.id))
