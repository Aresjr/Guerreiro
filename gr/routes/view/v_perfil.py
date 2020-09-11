from app import app
from flask import render_template
from flask_login import login_required, current_user

from gr.service.NivelHabilidadeService import nivel_habilidade_service


@app.route('/view/perfil')
@login_required
def v_perfil():
    usuario = current_user
    nhs = nivel_habilidade_service.get_nh_pai_usuario(usuario.id)
    print(nhs)
    return render_template('pages/perfil.html', usuario=usuario, nhs=nhs)
