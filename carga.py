from datetime import datetime

from app import db
from gr.model.atividades.Atividade import Atividade
from gr.model.atividades.Estagio import Estagio
from gr.model.usuario.TipoConquista import TipoConquista
from gr.model.usuario.Usuario import Usuario

ares = Usuario.query.filter(Usuario.username == 'ares').first()
if not ares:
    ares = Usuario(nome='Aristides Cândido Júnior', username='ares', email='ares@ares.dev.br')
    ares.set_password('aresroot')
    db.session.add(ares)
    db.session.commit()

dante = Usuario.query.filter(Usuario.username == 'dante').first()
if not dante:
    dante = Usuario(nome='Dante', username='dante', email='dante@ares.dev.br')
    dante.set_password('danteroot')
    db.session.add(dante)
    db.session.commit()

if Atividade.query.count() == 0:
    atividade1 = Atividade(codigo='1',      descricao='Primeira Atividade', usuarioExecucao=ares.id)
    atividade2 = Atividade(codigo='Dois',   descricao='Segunda Atividade',  usuarioExecucao=ares.id)
    atividade3 = Atividade(codigo='3-A',    descricao='Terceira Atividade', usuarioExecucao=ares.id)
    atividade4 = Atividade(descricao='Quarta Atividade',   usuarioExecucao=ares.id)
    atividade5 = Atividade(codigo='5',      descricao='Quinta Atividade',   usuarioExecucao=ares.id)
    atividade6 = Atividade(codigo='OS-123', descricao='Sexta Atividade',    usuarioExecucao=ares.id)
    db.session.add_all([atividade1, atividade2, atividade3, atividade4, atividade5, atividade6])
    db.session.commit()

if Estagio.query.count() == 0:
    estagioTodo = Estagio(titulo='TO DO', dataVigenciaInicio=datetime.now(), ordem=1)
    estagioDoing = Estagio(titulo='Doing', dataVigenciaInicio=datetime.now(), ordem=2)
    estagioTesting = Estagio(titulo='Testing', dataVigenciaInicio=datetime.now(), estagioTeste=True, ordem=3)
    estagioDone = Estagio(titulo='Done', dataVigenciaInicio=datetime.now(), estagioFinal=True, ordem=4)
    db.session.add_all([estagioTodo, estagioDoing, estagioTesting, estagioDone])
    db.session.commit()

# if db.session.query(AtividadeEstagio).count() == 0:
#     atividade1 = Atividade.query.get(1)
#     estagioTodo = Estagio.query.get(1)
#     atividadeEstagio1 = AtividadeEstagio.insert(atividade_id=atividade1.id, usuario_id=ares.id,
#                                                 estagio_id=estagioTodo.id)
#     db.session.add_all([atividadeEstagio1])
#     db.session.commit()

# if TipoConquista.query.count() == 0
    '''
tipoNotificacao = {
    'levelUp': {
        'id': 1,
        'titulo': 'Level Up!',
        'size': 'large',
        'icon': 'lvlup',
    },
    'skillUp': {
        'id': 2,
        'titulo': 'Habilidade Subiu',
        'size': 'small',
        'icon': 'skillup'
    },
    'aniversario': {
        'id': 3,
        'size': 'large',
        'icon': 'birthday-cake'
    },
    'aniversarioEmpresa': {
        'id': 4,
        'size': 'large',
        'icon': 'shield'
    },
    'feedback': {
        'id': 5,
        'size': 'large',
        'icon': 'talk'
    },
    'medalha': {

    }
}
    '''
    conquistaLevelUp = TipoConquista(titulo='Level Up!', destaque=True, icone='levelup')
    conquistaSkillUp = TipoConquista(titulo='Nível de Habilidade Up', destaque=False, icone='skillup')