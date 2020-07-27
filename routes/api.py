from flask import jsonify

from app import app


@app.route('/api/tarefas', methods=["POST", "GET"])
def api_tarefas():
    json = {"teste": "conteúdo teste"}
    return jsonify(json)
