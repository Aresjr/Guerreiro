from gr.dao.BaseDao import BaseDao
from gr.model.usuario.Habilidade import Habilidade


class HabilidadeDao(BaseDao):

    def purge_all(self):
        habilidades = self.get_all()
        for h in habilidades:
            if h.habPaiId != None:
                h.habPaiId = None
                self.upsert(h)
            self.purge(h)
        pass


habilidade_dao = HabilidadeDao(Habilidade)
