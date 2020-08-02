from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from model import Lang, Atividade, Usuario, Cargo, Empresa, Habilidade, Historico, Conquista, \
    NivelAcesso, RequisitoCargo, Setor, TipoConquista, Conquista, Xp, Vaga

manager.run()
