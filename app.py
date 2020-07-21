import logging
import os
from logging import Formatter, FileHandler

from flask import Flask, render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pgroot@localhost/guerreiro'
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
from model import Lang, Company, Department, Group, User, Role, Race
manager.run()


@app.route('/')
def home():
    return render_template('pages/home.html', users=[])


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    app.run()
