from gr.model.usuario.Xp import Xp


class XpDao:
    def __init__(self, model):
        self.model = model

    def get_by_atividadeid(self, atividadeid):
        return self.model.query.filter(self.model.atividadeId == atividadeid).all()


xp_dao = XpDao(Xp)
