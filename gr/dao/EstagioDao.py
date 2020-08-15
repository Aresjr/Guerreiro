from gr.model.atividades.Estagio import Estagio


class EstagioDao:
    def __init__(self, model):
        self.model = model

    def get_by_empresa(self, empresa_id):
        return self.model.query.filter(self.model.del_ == False).filter(self.model.empresaId == empresa_id).order_by(self.model.ordem.asc()).all()


estagio_dao = EstagioDao(Estagio)
