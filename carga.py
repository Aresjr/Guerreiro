from datetime import datetime

from app import db
from gr.model.atividades.Atividade import Atividade
from gr.model.atividades.Estagio import Estagio
from gr.model.atividades.TipoAtividade import TipoAtividade
from gr.model.usuario.Habilidade import Habilidade
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

tipoAtividade = TipoAtividade(descricao='')

ativ1 = Atividade(id=1, codigo='1', descricao='Desenvolver tela de Atividades', usuarioExecucao=ares.id)
ativ2 = Atividade(id=2, codigo='Dois', descricao='Desenvolver tela de Apontamentos', usuarioExecucao=ares.id)
ativ3 = Atividade(id=3, codigo='3-A', descricao='Modelagem de Dados', usuarioExecucao=ares.id)
ativ4 = Atividade(id=4, codigo=None, descricao='Quarta Atividade', usuarioExecucao=ares.id)
ativ5 = Atividade(id=5, codigo='5', descricao='Quinta Atividade', usuarioExecucao=ares.id)
ativ6 = Atividade(id=6, codigo='OS-123', descricao='Sexta Atividade', usuarioExecucao=ares.id)
if Atividade.query.count() == 0:
    db.session.add_all([ativ1, ativ2, ativ3, ativ4, ativ5, ativ6])

estagioTodo = Estagio(id=1, titulo='TO DO', dataVigenciaInicio=datetime.now(), ordem=1)
estagioDoing = Estagio(id=2, titulo='Doing', dataVigenciaInicio=datetime.now(), ordem=2)
estagioTesting = Estagio(id=3, titulo='Testing', dataVigenciaInicio=datetime.now(), estagioTeste=True, ordem=3)
estagioDone = Estagio(id=4, titulo='Done', dataVigenciaInicio=datetime.now(), estagioFinal=True, ordem=4)
if Estagio.query.count() == 0:
    db.session.add_all([estagioTodo, estagioDoing, estagioTesting, estagioDone])

conqLevelUp = TipoConquista(id=1, titulo='Level Up!', destaque=True, icone='levelup')
conqSkillUp = TipoConquista(id=2, titulo='Habilidade Subiu de Nível', destaque=False, icone='skillup')
if TipoConquista.query.count() == 0:
    db.session.add_all([conqLevelUp, conqSkillUp])

habProg = Habilidade(id=1, titulo='Programação')
habProgPython = Habilidade(id=2, titulo='Python', habPai=habProg.id)
habProgJs = Habilidade(id=3, titulo='Javascript', habPai=habProg.id)
habProgJava = Habilidade(id=4, titulo='Java', habPai=habProg.id)

habDB = Habilidade(id=5, titulo='Banco de Dados')
habPostgreSQL = Habilidade(id=6, titulo='PostgreSQL', habPai=habDB.id)
habOracle = Habilidade(id=7, titulo='Oracle', habPai=habDB.id)
habMongoDB = Habilidade(id=8, titulo='MongoDB', habPai=habDB.id)

habFrontEnd = Habilidade(id=9, titulo='Front End')
habFrontEndCss = Habilidade(id=10, titulo='HTML/CSS', habPai=habFrontEnd.id)
habFrontEndAngular = Habilidade(id=11, titulo='Angular', habPai=habFrontEnd.id)
habFrontEndVue = Habilidade(id=12, titulo='Vue', habPai=habFrontEnd.id)

engenhariaSoftware = Habilidade(id=13, titulo='Enenharia de Software')
habModelagemDados = Habilidade(id=14, titulo='Modelagem de Dados', habPai=engenhariaSoftware.id)

habAnalise = Habilidade(id=15, titulo='Análise')
habAnaliseSistema = Habilidade(id=16, titulo='Análise de Sistemas', habPai=habAnalise.id)
habAnaliseDados = Habilidade(id=17, titulo='Análise de Dados', habPai=habAnalise.id)

if Habilidade.query.count() == 0:
    db.session.add_all([habProg, habProgPython, habProgJs, habProgJava, habDB, habPostgreSQL, habMongoDB, habOracle,
                        habFrontEnd, habFrontEndCss, habFrontEndVue, habFrontEndAngular, engenhariaSoftware,
                        habModelagemDados, habAnalise, habAnaliseDados, habAnaliseSistema])




db.session.commit()
