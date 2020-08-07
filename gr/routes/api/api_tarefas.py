from flask import jsonify

from app import app


@app.route('/api/tarefas', methods=["POST"])
def api_tarefas_post():
    return jsonify()


@app.route('/api/tarefas', methods=["GET"])
def api_tarefas_get():
    json = {"teste": "conteúdo teste"}
    return jsonify(json)
