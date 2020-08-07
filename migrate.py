from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from gr.model import Lang, Atividade, Usuario, Cargo, Empresa, Habilidade, Conquista, \
    NivelAcesso, RequisitoCargo, Setor, TipoConquista, Xp, Vaga, Penalidade, Medalha, TipoAtividade, NivelHabilidade, \
    Estagio, TipoNotificacao, Notificacao

from gr.model.manyToMany import AtividadeHabilidade, HabilidadeTipoAtividade, NivelHabilidadeUsuario, AtividadeEstagio

manager.run()
