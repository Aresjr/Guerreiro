from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Lang, Company, Department, Group, User, Role, Race

Session = sessionmaker()
engine = create_engine('postgresql://postgres:pgroot@localhost/guerreiro')
Session.configure(bind=engine)
dbsession = Session()

langPt = Lang.Lang(code='pt', description='Português')
langEn = Lang.Lang(code='en', description='English')
dbsession.add_all([langPt, langEn])
dbsession.flush()

company = Company.Company(name='Philips', fantasyName='Philips Clinical Informatics', lang=langPt.id)
dbsession.add(company)
dbsession.flush()

departmentBilling = Department.Department(name='Faturamento', company=company.id)
dbsession.add(departmentBilling)
dbsession.flush()

group = Group.Group(name='Fat Público', department=departmentBilling.id)
dbsession.add(group)
dbsession.flush()

roleAdm = Role.Role(description='ADM')
roleEmployee = Role.Role(description='Employee')
roleAnalyst = Role.Role(description='Analyst')
dbsession.add_all([roleAdm, roleEmployee, roleAnalyst])
dbsession.flush()

raceGuerreiro = Race.Race(description='Guerreiro')
raceMago = Race.Race(description='Mago')
raceArqueiro = Race.Race(description='Arqueiro')
dbsession.add([raceGuerreiro, raceMago, raceArqueiro])
dbsession.flush()

userAres = User.User(name='Aristides Cândido Júnior', nickname='ares', role=roleEmployee.id, group=group.id,
                     email='aristidescandidojunior@gmail.com', race=raceGuerreiro.id)
userAres.set_password('qwer1234')

userAdm = User.User(name='Administrator', nickname='admin', role=roleAdm.id, email='admin@email.com')
userAdm.set_password('admin123')
dbsession.add([userAdm, userAres])
dbsession.flush()
