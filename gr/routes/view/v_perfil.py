from array import array

from app import app
from flask import render_template
from flask_login import login_required, current_user
from gr.service.NivelHabilidadeService import nivel_habilidade_service


@app.route('/view/perfil')
@login_required
def v_perfil():
    usuario = current_user
    nhs = nivel_habilidade_service.get_nh_usuario(usuario.id)
    v_nhs = {}
    for nh in nhs:
        if nh.habilidade.habPaiId is None:
            v_nhs[nh.habilidade.id] = vars(nh)
            v_nhs[nh.habilidade.id]['habFilho'] = []
            v_nhs[nh.habilidade.id]['habilidade'] = vars(nh.habilidade)
        else:
            hab_filho = vars(nh)
            hab_pai_id = nh.habilidade.habPaiId
            hab_filho['habilidade'] = vars(nh.habilidade)
            v_nhs[hab_pai_id]['habFilho'].append(hab_filho)
    return render_template('pages/perfil.html', usuario=usuario, nhs=v_nhs)
