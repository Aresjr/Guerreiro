from flask import render_template

from app import app


@app.route('/')
def home():
    return render_template('pages/home.html', title="Início", pageTitle="Início")
