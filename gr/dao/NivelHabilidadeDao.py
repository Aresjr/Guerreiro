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
        return self.model.query.filter(self.model.usuarioId == usuarioid).all()

    def get_nh_pai_usuario(self, usuarioid):
        return self.model.query.filter(self.model.usuarioId == usuarioid).filter(Habilidade.habPaiId == None).all()


nivel_habilidade_dao = NivelHabilidadeDao(NivelHabilidade)
