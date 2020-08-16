from app import app
from flask import jsonify, request
from flask_login import current_user
from gr.service.AtividadeService import atividade_service
from gr.service.EstagioService import estagio_service


@app.route('/api/atividades', methods=["GET"])
def api_atividades_get():
    usuario = current_user
    estagios_json = estagio_service.get_quadro_by_usuario(usuario)
    return jsonify(estagios_json)

@app.route('/api/atividade_estagio', methods=["POST"])
def api_atividade_estagio():
    usuario = current_user
    atividade_service.iniciar_atividade(usuario.id, request.form['atividade_id'], request.form['estagio_id'])
    return jsonify({'response': 'OK'})
