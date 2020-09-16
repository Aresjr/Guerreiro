from gr.dao.BaseDao import BaseDao
from gr.model.atividades.Estagio import Estagio


class EstagioDao(BaseDao):
    def get_by_empresa(self, empresa_id):
        return self.model.query.filter(self.model.del_ == False, self.model.empresaId == empresa_id).order_by(self.model.ordem.asc()).all()

    def get_by_titulo(self, titulo):
        return self.model.query.filter(self.model.titulo == titulo).first()

    def get(self, estagio_id):
        return self.model.query.get(estagio_id)

    def get_by_empresa_ordem(self, empresa_id, ordemInicial, ordemFinal):
        return self.model.query.filter(self.model.del_ == False, self.model.empresaId == empresa_id, self.model.ordem >= ordemInicial, self.model.ordem <= ordemFinal).order_by(self.model.ordem.asc()).all()


estagio_dao = EstagioDao(Estagio)
