from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# noinspection PyUnresolvedReferences
from gr.model.atividades import Atividade, Estagio, TipoAtividade
# noinspection PyUnresolvedReferences
from gr.model.empresa import Empresa, Setor
# noinspection PyUnresolvedReferences
from gr.model.manyToMany import HabilidadeTipoAtividade, AtividadeEstagio
# noinspection PyUnresolvedReferences
from gr.model.notificacao import Notificacao, TipoNotificacao
# noinspection PyUnresolvedReferences
from gr.model.usuario import Conquista, Habilidade, Medalha, NivelAcesso, NivelHabilidade, TipoConquista, Usuario, Xp
# noinspection PyUnresolvedReferences
from gr.model.vaga import Cargo, RequisitoCargo, Vaga
# noinspection PyUnresolvedReferences
from gr.model import Apontamento, Lang, Penalidade

manager.run()
