from sqlalchemy.orm import sessionmaker

from model.Company import Company
from model.Department import Department
from model.Group import Group
from model.Lang import Lang
from model.User import User
#
# Session = sessionmaker()
# session = Session()
#
# langPt = Lang(code='pt-br', description='Português (Brasil)')
# #session.add(langPt)
# #session.commit()
# langEn = Lang(code='en', description='English')
# #session.add(langEn)
# company = Company(name='Philips', lang=langPt.id)
# #session.add(company)
# departmentBilling = Department(name='Faturamento', company=company.id)
# #session.add(departmentBilling)
# group = Group(name='Fat Público', department=departmentBilling.id)
# #session.add(group)
# user = User(name='Aristides Cândido Júnior', nickname='ares', group=group.id)
# #session.add(user)
# #session.commit()
# session.add_all([
#     langPt,
#     langEn,
#     company,
#     departmentBilling,
#     group,
#     user,
# ])
# session.commit()
