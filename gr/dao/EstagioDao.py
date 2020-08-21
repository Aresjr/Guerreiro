from app import db
from gr.model.atividades.Estagio import Estagio


class EstagioDao:
    def __init__(self, model):
        self.model = model

    def get_by_empresa(self, empresa_id):
        return self.model.query.filter(self.model.del_ == False).filter(self.model.empresaId == empresa_id).order_by(self.model.ordem.asc()).all()

    def get(self, estagio_id):
        return self.model.query.get(estagio_id)

    def get_all(self):
        return self.model.query.all()

    def update(self, estagio):
        db.session.add(estagio)
        return db.session.commit()

    def update_all(self, estagios):
        db.session.add_all(estagios)
        return db.session.commit()

    def get_by_empresa_ordem(self, empresa_id, ordemInicial, ordemFinal):
        return self.model.query.filter(self.model.del_ == False).filter(self.model.empresaId == empresa_id).filter(self.model.ordem >= ordemInicial).filter(self.model.ordem <= ordemFinal).order_by(self.model.ordem.asc()).all()


estagio_dao = EstagioDao(Estagio)
