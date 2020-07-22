from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Lang, Empresa, Setor, Grupo, Usuario, NivelAcesso, Raca

Session = sessionmaker()
engine = create_engine('postgresql://postgres:pgroot@localhost/guerreiro')
Session.configure(bind=engine)
dbsession = Session()

langPt = Lang.Lang(code='pt', description='Português')
langEn = Lang.Lang(code='en', description='English')
dbsession.add_all([langPt, langEn])
dbsession.flush()

company = Empresa.Empresa(name='Philips', fantasyName='Philips Clinical Informatics', lang=langPt.id)
dbsession.add(company)
dbsession.flush()

departmentBilling = Setor.Department(name='Faturamento', company=company.id)
dbsession.add(departmentBilling)
dbsession.flush()

group = Grupo.Grupo(name='Fat Público', department=departmentBilling.id)
dbsession.add(group)
dbsession.flush()

roleAdm = NivelAcesso.NivelAcesso(description='ADM')
roleEmployee = NivelAcesso.NivelAcesso(description='Employee')
roleAnalyst = NivelAcesso.NivelAcesso(description='Analyst')
dbsession.add_all([roleAdm, roleEmployee, roleAnalyst])
dbsession.flush()

raceGuerreiro = Raca.Race(description='Guerreiro')
raceMago = Raca.Race(description='Mago')
raceArqueiro = Raca.Race(description='Arqueiro')
dbsession.add([raceGuerreiro, raceMago, raceArqueiro])
dbsession.flush()

userAres = Usuario.Usuario(name='Aristides Cândido Júnior', nickname='ares', role=roleEmployee.id, group=group.id,
                           email='aristidescandidojunior@gmail.com', race=raceGuerreiro.id)
userAres.set_password('qwer1234')

userAdm = Usuario.Usuario(name='Administrator', nickname='admin', role=roleAdm.id, email='admin@email.com')
userAdm.set_password('admin123')
dbsession.add([userAdm, userAres])
dbsession.flush()
