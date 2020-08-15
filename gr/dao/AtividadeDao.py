from gr.model.atividades.Atividade import Atividade

class AtividadeDao:
    def __init__(self, model):
        self.model = model

    def get_by_userid(self, userid):
        return self.model.query.filter(self.model.del_ == False, self.model.usuarioExecucaoId == userid).all()

    def get_xp_nao_contabilizados(self, userid):
        return self.model.query.filter(self.model.xpContabilizado == False).filter(self.model.usuarioExecucaoId == userid).all()


atividade_dao = AtividadeDao(Atividade)
