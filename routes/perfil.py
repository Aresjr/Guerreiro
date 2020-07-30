from flask import render_template

from app import app
from model.Cargo import Cargo
from model.Usuario import Usuario


@app.route('/perfil')
def perfil():
    cargo = Cargo(titulo="Programador")
    usuario = Usuario(nome="Aristides Cândido Júnior", nickname="Ares", level=30, cargo=cargo,
                      email="aristidescandidojunior@gmail.com")
    return render_template('pages/perfil.html', title="Início", pageTitle="Início", usuario=usuario)
