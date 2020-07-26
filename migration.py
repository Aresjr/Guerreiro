from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from model import Lang, Empresa, Setor, Grupo, Usuario, NivelAcesso, Raca, Cargo

manager.run()
