from gr.dao.BaseDao import BaseDao
from gr.model.usuario.Xp import Xp


class XpDao(BaseDao):
    def get_by_atividadeid(self, atividadeid):
        return self.model.query.filter(self.model.atividadeId == atividadeid).all()


xp_dao = XpDao(Xp)
