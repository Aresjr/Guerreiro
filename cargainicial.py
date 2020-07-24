from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Lang, Empresa, Setor, Grupo, Usuario, NivelAcesso, Cargo

Session = sessionmaker()
engine = create_engine('postgresql://postgres:pgroot@localhost/guerreiro')
Session.configure(bind=engine)
dbsession = Session()

langDe = Lang.Lang(codigo='de', desc='Deutschland')
dbsession.add(langDe)
dbsession.commit()

empresa = Empresa.Empresa(nome='Philips', nomeFantasia='Philips Clinical Informatics', lang=langPt.id)
dbsession.add(empresa)
dbsession.commit()

setorFaturamento = Setor.Setor(nome='Faturamento', empresa=empresa.id)
dbsession.add(setorFaturamento)
dbsession.commit()

grupo = Grupo.Grupo(nome='Fat Específico', setor=setorFaturamento.id)
dbsession.add(grupo)
dbsession.commit()

nivelAcessoAdm = NivelAcesso.NivelAcesso(desc='ADM')

cargoFuncionario = Cargo.Cargo(desc='Funcionário')
cargoAnalista = Cargo.Cargo(desc='Analyst')
dbsession.add_all([nivelAcessoAdm, cargoFuncionario, cargoAnalista])
dbsession.commit()

userAres = Usuario.Usuario(nome='Aristides Cândido Júnior', nickname='ares', cargo=cargoFuncionario.id, grupo=grupo.id,
                           email='aristidescandidojunior@gmail.com')
userAres.set_password('qwer1234')

userAdm = Usuario.Usuario(nome='Administrator', nickname='admin', nivelAcesso=nivelAcessoAdm.id, email='admin@email.com')
userAdm.set_password('admin123')
dbsession.add_all([userAdm, userAres])
dbsession.commit()
