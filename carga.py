from datetime import datetime

from app import db
from gr.model.atividades.Atividade import Atividade
from gr.model.atividades.Estagio import Estagio
from gr.model.usuario.TipoConquista import TipoConquista
from gr.model.usuario.Usuario import Usuario

ares = Usuario(id=1, nome='Aristides Cândido Júnior', username='ares', email='ares@ares.dev.br')
ares.set_password('aresroot')
if not Usuario.query.filter(Usuario.username == 'ares').first():
    db.session.add(ares)

dante = Usuario(id=2, nome='Dante', username='dante', email='dante@ares.dev.br')
dante.set_password('danteroot')
if not Usuario.query.filter(Usuario.username == 'dante').first():
    db.session.add(dante)

atividade1 = Atividade(id=1, codigo='1', descricao='Primeira Atividade', usuarioExecucao=ares.id)
atividade2 = Atividade(id=2, codigo='Dois', descricao='Segunda Atividade', usuarioExecucao=ares.id)
atividade3 = Atividade(id=3, codigo='3-A', descricao='Terceira Atividade', usuarioExecucao=ares.id)
atividade4 = Atividade(id=4, codigo=None, descricao='Quarta Atividade', usuarioExecucao=ares.id)
atividade5 = Atividade(id=5, codigo='5', descricao='Quinta Atividade', usuarioExecucao=ares.id)
atividade6 = Atividade(id=6, codigo='OS-123', descricao='Sexta Atividade', usuarioExecucao=ares.id)
if Atividade.query.count() == 0:
    db.session.add_all([atividade1, atividade2, atividade3, atividade4, atividade5, atividade6])

estagioTodo = Estagio(id=1, titulo='TO DO', dataVigenciaInicio=datetime.now(), ordem=1)
estagioDoing = Estagio(id=2, titulo='Doing', dataVigenciaInicio=datetime.now(), ordem=2)
estagioTesting = Estagio(id=3, titulo='Testing', dataVigenciaInicio=datetime.now(), estagioTeste=True, ordem=3)
estagioDone = Estagio(id=4, titulo='Done', dataVigenciaInicio=datetime.now(), estagioFinal=True, ordem=4)
if Estagio.query.count() == 0:
    db.session.add_all([estagioTodo, estagioDoing, estagioTesting, estagioDone])

conquistaLevelUp = TipoConquista(id=1, titulo='Level Up!', destaque=True, icone='levelup')
conquistaSkillUp = TipoConquista(id=2, titulo='Habilidade Subiu de Nível', destaque=False, icone='skillup')
if TipoConquista.query.count() == 0:
    db.session.add_all([conquistaLevelUp, conquistaSkillUp])

db.session.commit()
