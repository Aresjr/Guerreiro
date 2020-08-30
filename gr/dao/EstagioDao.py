from app import db
from gr.dao.BaseDao import BaseDao
from gr.model.atividades.Estagio import Estagio


class EstagioDao(BaseDao):
    def get_by_empresa(self, empresa_id):
        return self.model.query.filter(self.model.del_ == False).filter(self.model.empresaId == empresa_id).order_by(self.model.ordem.asc()).all()

    def get_by_titulo(self, titulo):
        return self.model.query.filter(self.model.titulo == titulo).first()

    def get(self, estagio_id):
        return self.model.query.get(estagio_id)

    def update(self, estagio):
        db.session.add(estagio)
        return db.session.commit()

    def update_all(self, estagios):
        db.session.add_all(estagios)
        return db.session.commit()

    def get_by_empresa_ordem(self, empresa_id, ordemInicial, ordemFinal):
        return self.model.query.filter(self.model.del_ == False).filter(self.model.empresaId == empresa_id).filter(self.model.ordem >= ordemInicial).filter(self.model.ordem <= ordemFinal).order_by(self.model.ordem.asc()).all()


estagio_dao = EstagioDao(Estagio)
