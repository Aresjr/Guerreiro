from app import db
from gr.model.atividades.Atividade import Atividade

class AtividadeDao:
    def __init__(self, model):
        self.model = model

    def get_by_id(self, id):
        return self.model.query.get(id)

    def get_all(self):
        return self.model.query.all()

    def get_by_userid(self, userid):
        return self.model.query.filter(self.model.del_ == False, self.model.usuarioExecucaoId == userid).all()

    def get_xp_nao_contabilizados(self, userid):
        return self.model.query.filter(self.model.del_ == False, self.model.usuarioExecucaoId == userid, self.model.xpContabilizado == False).all()

    def update(self, atividade):
        db.session.add(atividade)
        return db.session.commit()


atividade_dao = AtividadeDao(Atividade)
