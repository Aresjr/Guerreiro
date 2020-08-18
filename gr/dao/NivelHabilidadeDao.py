from app import db
from gr.model.usuario.NivelHabilidade import NivelHabilidade


class NivelHabilidadeDao:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.query.all()

    def get_or_insert_nh(self, usuarioid, habilidadeid):
        nh = self.model.query.filter(self.model.usuarioId == usuarioid).filter(
            self.model.habilidadeId == habilidadeid).first()
        if not nh:
            nh = self.insert(usuarioid, habilidadeid)
        return nh

    def insert(self, usuarioid, habilidadeid):
        nh = NivelHabilidade(usuarioId=usuarioid, habilidadeId=habilidadeid)
        db.session.add(nh)
        db.session.commit()
        return nh

    def update(self, nivel_habilidade):
        db.session.add(nivel_habilidade)
        db.session.commit()
        return nivel_habilidade

    def purge(self, nivel_habilidade):
        db.session.execute(nivel_habilidade.delete())
        db.session.commit()

    def purge_all(self):
        nhs = self.get_all()
        for nh in nhs:
            db.session.delete(nh)
            db.session.commit()


nivel_habilidade_dao = NivelHabilidadeDao(NivelHabilidade)
