from app import app, db
from flask import jsonify, request
from flask_login import login_required, current_user
from gr.dao.EstagioDao import estagio_dao
from gr.model.atividades.Atividade import Atividade


@app.route('/api/atividades', methods=["GET"])
@login_required
def api_atividades_get():
    usuario = current_user
    estagios = estagio_dao.get_by_empresa(usuario.setor.empresa.id)
    estagios_json = []

    for estagio in estagios:

        itens = []
        for atividade in estagio.atividades:
            itens.append({
                'title': atividade.codigo,
                'descricao': atividade.descricao,
                'executor': atividade.usuarioExecucao.username,
                'id': str(atividade.id)
            })

        estagios_json.append({
                'id': str(estagio.id),
                'title': estagio.titulo,
                'class': 'kb-info',
                'item': itens,
                'dragTo': ['1', '2', '3', '4']
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
