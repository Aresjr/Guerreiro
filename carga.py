from datetime import datetime

from app import db
from model.Atividade import Atividade
from model.Usuario import Usuario
from model.manyToMany.AtividadeUsuario import AtividadeUsuario

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
    atividade1 = Atividade(codigo='1',      descricao='Primeira Atividade', dataInicio=datetime.now())
    atividade2 = Atividade(codigo='Dois',   descricao='Segunda Atividade',  dataInicio=datetime.now())
    atividade3 = Atividade(codigo='3-A',    descricao='Terceira Atividade', dataInicio=datetime.now())
    atividade4 = Atividade(codigo='Four',   descricao='Quarta Atividade',   dataInicio=datetime.now())
    atividade5 = Atividade(codigo='5',      descricao='Quinta Atividade',   dataInicio=datetime.now())
    atividade6 = Atividade(codigo='OS-123', descricao='Sexta Atividade',    dataInicio=datetime.now())
    db.session.add_all([atividade1, atividade2, atividade3, atividade4, atividade5, atividade6])
    db.session.commit()

if db.session.query(AtividadeUsuario).count() == 0:
    db.session.execute(AtividadeUsuario.insert().values(atividade_id=1, usuario_id=ares.id))
    db.session.execute(AtividadeUsuario.insert().values(atividade_id=2, usuario_id=ares.id))
    db.session.execute(AtividadeUsuario.insert().values(atividade_id=3, usuario_id=ares.id))
    db.session.execute(AtividadeUsuario.insert().values(atividade_id=4, usuario_id=ares.id))
    db.session.execute(AtividadeUsuario.insert().values(atividade_id=5, usuario_id=ares.id))
    db.session.execute(AtividadeUsuario.insert().values(atividade_id=6, usuario_id=ares.id))
    db.session.commit()
