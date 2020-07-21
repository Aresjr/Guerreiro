from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Lang, Company, Department, Group, User


Session = sessionmaker()
engine = create_engine('postgresql://postgres:pgroot@localhost/guerreiro')
Session.configure(bind=engine)
session = Session()


langPt = Lang.Lang(code='pt', description='Português')
session.add(langPt)
session.commit()

langEn = Lang.Lang(code='en', description='English')
session.add(langEn)
session.commit()

company = Company.Company(name='Philips', lang=langPt.id)
session.add(company)
session.commit()

departmentBilling = Department.Department(name='Faturamento', company=company.id)
session.add(departmentBilling)
session.commit()

group = Group.Group(name='Fat Público', department=departmentBilling.id)
session.add(group)
session.commit()

user = User.User(name='Aristides Cândido Júnior', nickname='ares', group=group.id, email='aristidescandidojunior@gmail.com')
session.add(user)
session.commit()
