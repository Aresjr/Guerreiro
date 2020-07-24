from sqlalchemy import create_engine, table
from sqlalchemy.orm import sessionmaker
from model import Lang, Empresa, Setor, Grupo, NivelAcesso, Cargo
from model.Usuario import Usuario

SQLALCHEMY_TRACK_MODIFICATIONS = False
Session = sessionmaker()
engine = create_engine('postgresql://postgres:pgroot@localhost/guerreiro')
Session.configure(bind=engine)
dbsession = Session()

# dbsession.add(object)
# dbsession.commit()

usuario = dbsession.query(Usuario).get(4)
print(usuario.nickname)
