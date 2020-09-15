from app import app
from flask import render_template, flash, redirect, url_for


@app.errorhandler(401)
def _401(e):
    flash('O tempo de login expirou, você deve fazer login novamente', 'danger')
    return redirect(url_for('login')), 401

@app.errorhandler(404)
def _404(e):
    return render_template('pages/404.html'), 404
