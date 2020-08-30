from app import app
from flask import jsonify, request
from flask_login import current_user

from gr.dao.AtividadeDao import atividade_dao
from gr.model.atividades.Atividade import Atividade
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
    estagio_service.alterar_ordem(int(request.form['estagio_id']), int(request.form['ordem']))
    return jsonify({'response': 'OK'})

@app.route('/api/atividade_nova', methods=["POST"])
def api_atividade_nova():
    try:
        atividade = Atividade(titulo=request.form['titulo'], descricao=request.form['descricao'], usuarioExecucaoId=request.form['usuarioExecucaoId'], estagioId=request.form['estagioId'])
        atividade_dao.add(atividade)
        return jsonify({'response': 'OK'})
    except Exception as e:
        return jsonify({'error': str(e)})
