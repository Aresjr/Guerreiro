from flask import Flask, render_template
from flask_mongoengine import MongoEngine
import logging
from logging import Formatter, FileHandler
from model.User import User
import os

app = Flask(__name__)
app.config.from_object('config')
app.config['MONGODB_SETTINGS'] = {
    "db": "guerreiro",
}
db = MongoEngine(app)

@app.route('/')
def home():
    return render_template('pages/home.html', users=User.objects)


@app.errorhandler(500)
def internal_error(error):
    # db_session.rollback()
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