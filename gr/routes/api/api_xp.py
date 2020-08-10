from app import app
from flask import jsonify


@app.route('/api/xp', methods=["POST"])
def api_xp_post():
    return jsonify()
