from app import app
from flask import render_template
from flask_login import current_user


@app.route('/')
def index():
    usuario = current_user
    return render_template('pages/pagina-inicial.html', usuario=usuario)
