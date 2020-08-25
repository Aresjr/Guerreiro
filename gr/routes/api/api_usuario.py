from flask_login import current_user

from app import app
from flask import jsonify

from gr.service.UsuarioService import usuario_service


@app.route('/api/get_usuarios_empresa', methods=["GET"])
def api_get_usuarios_empresa():
    return jsonify(usuario_service.get_usuarios_empresa(current_user.empresaId))
