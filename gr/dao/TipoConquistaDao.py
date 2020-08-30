from gr.dao.BaseDao import BaseDao
from gr.model.usuario.TipoConquista import TipoConquista


class TipoConquistaDao(BaseDao):
    def get_by_titulo(self, titulo):
        return self.model.query.filter(self.model.titulo == titulo).first()

    def get_by_icone(self, icone):
        return self.model.query.filter(self.model.icone == icone).first()


tipo_conquista_dao = TipoConquistaDao(TipoConquista)
