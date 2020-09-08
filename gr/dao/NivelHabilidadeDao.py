from app import db
from gr.dao.BaseDao import BaseDao
from gr.model.usuario.NivelHabilidade import NivelHabilidade


class NivelHabilidadeDao(BaseDao):
    def get_or_insert_nh(self, usuarioid, habilidadeid):
        nh = self.model.query.filter(self.model.usuarioId == usuarioid).filter(
            self.model.habilidadeId == habilidadeid).first()
        if not nh:
            nh = self.upsert(NivelHabilidade(usuarioId=usuarioid, habilidadeId=habilidadeid))
        return nh

    def purge(self, nivel_habilidade):
        db.session.execute(nivel_habilidade.delete())
        db.session.commit()


nivel_habilidade_dao = NivelHabilidadeDao(NivelHabilidade)
