from flask import render_template

from app import app
from model.Cargo import Cargo
from model.Usuario import Usuario


@app.route('/')
def home():
    cargo = Cargo(desc="Programador")
    usuario = Usuario(nome="Aristides Cândido Júnior", nickname="Ares", level=30, cargo=cargo)
    return render_template('pages/home.html', title="Início", pageTitle="Início", usuario=usuario)
