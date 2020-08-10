from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from gr.model.atividades import Atividade, Estagio, TipoAtividade
from gr.model.empresa import Empresa, Setor
from gr.model.manyToMany import HabilidadeTipoAtividade, NivelHabilidadeUsuario, AtividadeEstagio
from gr.model.notificacao import Notificacao, TipoNotificacao
from gr.model.usuario import Conquista, Habilidade, Medalha, NivelAcesso, NivelHabilidade, TipoConquista, Usuario, Xp
from gr.model.vaga import Cargo, RequisitoCargo, Vaga
from gr.model import Apontamento, Lang, Penalidade

manager.run()
