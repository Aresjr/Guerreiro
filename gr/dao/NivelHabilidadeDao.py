from gr.dao.BaseDao import BaseDao
from gr.model.usuario.Habilidade import Habilidade
from gr.model.usuario.NivelHabilidade import NivelHabilidade


class NivelHabilidadeDao(BaseDao):
    def get_or_insert_nh(self, usuarioid, habilidadeid):
        nh = self.model.query.filter(self.model.usuarioId == usuarioid).filter(
            self.model.habilidadeId == habilidadeid).first()
        if not nh:
            nh = self.upsert(NivelHabilidade(usuarioId=usuarioid, habilidadeId=habilidadeid))
        return nh

    def get_by_usuario(self, usuarioid):
        return self.model.query.join(Habilidade).filter(self.model.usuarioId == usuarioid).order_by(Habilidade.habPaiId, self.model.level.desc(), self.model.currentXp.desc()).all()


nivel_habilidade_dao = NivelHabilidadeDao(NivelHabilidade)
