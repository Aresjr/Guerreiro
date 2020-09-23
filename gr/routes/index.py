from app import app
from flask import render_template
from flask_login import current_user


@app.route('/')
def index():
    usuario = current_user
    if usuario.is_anonymous:
        return render_template('pages/pagina-guerreiro.html', titulo='Suba de Nível na sua carreira')
    return render_template('layouts/pagina-inicial.html', usuario=usuario)

@app.route('/cadastrar')
def cadastrar():
    return render_template('pages/cadastrar.html', titulo='Cadastre-se')
