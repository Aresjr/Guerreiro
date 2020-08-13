from app import app
from flask import render_template
from flask_login import login_required, current_user

from gr.model.atividades.Estagio import Estagio


@app.route('/quadro', methods=['GET'])
@login_required
def quadro():
    usuario = current_user
    estagios = Estagio.query.filter(Estagio.del_ == False)
    qt_atividade_linha = estagios.count()

    estagios_json = []
    drag_to = []

    for estagio in estagios:
        drag_to.append(str(estagio.id))

        itens = []
        for atividade in estagio.atividades:
            itens.append({
                'title': atividade.descricao
            })

        estagios_json.append({
                'id': str(estagio.id),
                'title': estagio.titulo,
                'class': 'kb-info',
                'item': itens,
                'dragTo': ['3', '4']
        })

    return render_template('pages/quadros.html', title="Quadro de Atividades", usuario=usuario,
                           estagios=estagios_json,
                           qt_atividade_linha=qt_atividade_linha)
