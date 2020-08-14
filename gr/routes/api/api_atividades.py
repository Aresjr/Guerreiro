from flask_login import login_required

from app import app, db
from flask import jsonify, request

from gr.model.atividades.Atividade import Atividade
from gr.model.atividades.Estagio import Estagio


@app.route('/api/atividades', methods=["GET"])
@login_required
def api_atividades_get():
    estagios = Estagio.query.filter(Estagio.del_ == False)
    estagios_json = []

    for estagio in estagios:

        itens = []
        for atividade in estagio.atividades:
            itens.append({
                'title': atividade.descricao,
                'id': str(atividade.id)
            })

        estagios_json.append({
                'id': str(estagio.id),
                'title': estagio.titulo,
                'class': 'kb-info',
                'item': itens,
                'dragTo': ['3', '4']
        })

    return jsonify(estagios_json)

@app.route('/api/atividade_estagio', methods=["POST"])
@login_required
def api_atividade_estagio():
    atividade_id = request.form['atividade_id']
    estagio_id = request.form['estagio_id']

    atividade = Atividade.query.get(atividade_id)
    atividade.estagioId = estagio_id
    db.session.add(atividade)
    db.session.commit()

    return jsonify({'response':'OK'})
