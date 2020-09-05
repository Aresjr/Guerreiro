from app import app
from flask import render_template
from flask_login import login_required


@app.route('/view/kanban')
@login_required
def v_kanban():
    return render_template('pages/kanban.html')
