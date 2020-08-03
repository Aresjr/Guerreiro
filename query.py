from app import db
from model.Atividade import Atividade
from model.Usuario import Usuario
from model.manyToMany.AtividadeUsuario import AtividadeUsuario

usuarios = Usuario.query.filter(Usuario.username == 'ares')

for usuario in usuarios:
    print(usuario)

# atividade1 = Atividade(codigo='1',      descricao='Primeira Atividade')
# atividade2 = Atividade(codigo='Dois',   descricao='Segunda Atividade')
# atividade3 = Atividade(codigo='3-A',    descricao='Terceira Atividade')
# atividade4 = Atividade(codigo='Four',   descricao='Quarta Atividade')
# atividade5 = Atividade(codigo='5',      descricao='Quinta Atividade')
# atividade6 = Atividade(codigo='OS-123', descricao='Sexta Atividade')
# db.session.add_all([atividade1, atividade2, atividade3])
# db.session.commit()

atividades = db.session.query(AtividadeUsuario).filter_by(usuario_id=1)
# atividades = AtividadeUsuario.query.filter_by(usuario=1)
for atividade in atividades:
    print(atividade)
