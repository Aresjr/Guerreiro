from datetime import datetime

from app import db
from model.Atividade import Atividade
from model.Estagio import Estagio
from model.Usuario import Usuario

ares = Usuario.query.filter(Usuario.username == 'ares').first()
if not ares:
    ares = Usuario(nome='Aristides Cândido Júnior', username='ares', email='ares@ares.dev.br')
    ares.set_password('aresroot')
    db.session.add(ares)
    db.session.commit()

dante = Usuario.query.filter(Usuario.username == 'ares').first()
if not dante:
    dante = Usuario(nome='Aristides Cândido Júnior', username='ares', email='ares@ares.dev.br')
    dante.set_password('danteroot')
    db.session.add(dante)
    db.session.commit()

if Atividade.query.count() == 0:
    atividade1 = Atividade(codigo='1',      descricao='Primeira Atividade', dataInicio=datetime.now(),
                           usuarioId=ares.id)
    atividade2 = Atividade(codigo='Dois',   descricao='Segunda Atividade',  dataInicio=datetime.now(),
                           usuarioId=ares.id)
    atividade3 = Atividade(codigo='3-A',    descricao='Terceira Atividade', dataInicio=datetime.now(),
                           usuarioId=ares.id)
    atividade4 = Atividade(codigo='Four',   descricao='Quarta Atividade',   dataInicio=datetime.now(),
                           usuarioId=ares.id)
    atividade5 = Atividade(codigo='5',      descricao='Quinta Atividade',   dataInicio=datetime.now(),
                           usuarioId=ares.id)
    atividade6 = Atividade(codigo='OS-123', descricao='Sexta Atividade',    dataInicio=datetime.now(),
                           usuarioId=ares.id)
    db.session.add_all([atividade1, atividade2, atividade3, atividade4, atividade5, atividade6])
    db.session.commit()

if Estagio.query.count() == 0:
    estagioTodo = Estagio(titulo='TO DO', dataVigenciaInicio=datetime.now())
    estagioDoing = Estagio(titulo='Doing', dataVigenciaInicio=datetime.now())
    estagioTesting = Estagio(titulo='Testing', dataVigenciaInicio=datetime.now(), estagioTeste=True)
    estagioDone = Estagio(titulo='Done', dataVigenciaInicio=datetime.now(), estagioFinal=True)
    db.session.add_all([estagioTodo, estagioDoing, estagioTesting, estagioDone])
    db.session.commit()
