from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from model import Lang, Atividade, Usuario, Cargo, Empresa, Habilidade, Historico, Conquista, \
    NivelAcesso, RequisitoCargo, Setor, TipoConquista, Xp, Vaga, Penalidade, Medalha, TipoAtividade, NivelHabilidade, \
    Estagio

from model.manyToMany import AtividadeHabilidade, HabilidadeTipoAtividade, NivelHabilidadeUsuario, AtividadeEstagio

manager.run()
