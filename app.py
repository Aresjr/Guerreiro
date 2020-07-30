import logging
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging import Formatter, FileHandler


app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pgroot@localhost/guerreiro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TESTING'] = True
app.config['FLASK_ENV'] = 'development'
db = SQLAlchemy(app)

# MIGRATION
import migration

from routes import index, perfil, api

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
