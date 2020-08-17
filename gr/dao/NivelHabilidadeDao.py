from app import db
from gr.model.usuario.NivelHabilidade import NivelHabilidade


class NivelHabilidadeDao:
    def __init__(self, model):
        self.model = model

    def get_nivel_by_usuario_habilidade(self, usuarioid, habilidadeid):
        return self.model.query.filter(self.model.usuarioId == usuarioid).filter(self.model.habilidadeId == habilidadeid).first()

    def insert(self, usuarioid, habilidadeid):
        db.session.add(NivelHabilidade(usuarioId=usuarioid, habilidadeId=habilidadeid))
        return db.session.commit()

    def update(self, nivel_habilidade):
        db.session.add(nivel_habilidade)
        return db.session.commit()


nivel_habilidade_dao = NivelHabilidadeDao(NivelHabilidade)
