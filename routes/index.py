from flask import render_template
from flask_login import current_user

from app import app


@app.route('/')
def home():
    usuario = current_user
    return render_template('pages/home.html', title="Início", pageTitle="Início", usuario=usuario)
