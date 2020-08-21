from app import app
from flask import jsonify, request
from flask_login import current_user
from gr.service.AtividadeService import atividade_service
from gr.service.EstagioService import estagio_service


@app.route('/api/atividades', methods=["GET"])
def api_atividades_get():
    return jsonify(estagio_service.get_quadro_by_usuario(current_user))

@app.route('/api/trocar_estagio_atividade', methods=["POST"])
def api_trocar_estagio_atividade():
    usuario = current_user
    atividade_service.iniciar_atividade(usuario.id, int(request.form['atividade_id']), int(request.form['estagio_id']))
    return jsonify({'response': 'OK'})

@app.route('/api/trocar_ordem_estagio', methods=["POST"])
def api_trocar_ordem_estagio():
    usuario = current_user
    atividade_service.iniciar_atividade(usuario.id, int(request.form['estagio_id']), int(request.form['ordem']))
    return jsonify({'response': 'OK'})
