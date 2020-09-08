from gr.dao.BaseDao import BaseDao
from gr.model.atividades.Atividade import Atividade

class AtividadeDao(BaseDao):
    def get_by_userid(self, userid):
        return self.model.query.filter(self.model.del_ == False, self.model.usuarioExecucaoId == userid).all()

    def get_xp_nao_contabilizados(self, userid):
        return self.model.query.filter(self.model.del_ == False, self.model.usuarioExecucaoId == userid, self.model.xpContabilizado == False).all()


atividade_dao = AtividadeDao(Atividade)
