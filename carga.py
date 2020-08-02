from app import db
from model.Usuario import Usuario

usuario = Usuario(nome='Aristides Cândido Júnior', username='ares', email='ares@ares.dev.br')
usuario.set_password('aresroot')
db.session.add(usuario)
db.session.commit()

print(usuario.id)
