from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Lang, Empresa, Setor, Usuario, NivelAcesso, Cargo

Session = sessionmaker()
engine = create_engine('postgresql://postgres:pgroot@localhost/guerreiro')
Session.configure(bind=engine)
dbsession = Session()

langPt = Lang.Lang(codigo='pt', descricao='Português')
dbsession.add(langPt)
dbsession.commit()

empresa = Empresa.Empresa(nome='Philips', nomeFantasia='Philips Clinical Informatics', lang=langPt.id)
dbsession.add(empresa)
dbsession.commit()

setorFaturamento = Setor.Setor(nome='Faturamento', empresa=empresa.id)
dbsession.add(setorFaturamento)
dbsession.commit()

nivelAcessoAdm = NivelAcesso.NivelAcesso(descricao='ADM', criaUsuario=True, criaVaga=True, criaCargo=True,
                                         criaAtividades=True)

cargoFuncionario = Cargo.Cargo(titulo='Funcionário')
cargoAnalista = Cargo.Cargo(titulo='Analyst')
dbsession.add_all([nivelAcessoAdm, cargoFuncionario, cargoAnalista])
dbsession.commit()

userAres = Usuario.Usuario(nome='Aristides Cândido Júnior', nickname='ares', cargo=cargoFuncionario.id,
                           setor=setorFaturamento.id, email='aristidescandidojunior@gmail.com')
userAres.set_password('qwer1234')

userAdm = Usuario.Usuario(nome='Administrator', nickname='admin', nivelAcesso=nivelAcessoAdm.id,
                          email='admin@email.com')
userAdm.set_password('admin123')
dbsession.add_all([userAdm, userAres])
dbsession.commit()
