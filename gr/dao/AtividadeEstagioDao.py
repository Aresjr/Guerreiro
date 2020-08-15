from app import db
from gr.model.manyToMany.AtividadeEstagio import AtividadeEstagio


class AtividadeEstagioDao:
    def __init__(self, model):
        self.model = model

    def get_by_id(self, atividade, atividadeid):
        return db.session.query(self.model).filter_by(atividade_id=atividadeid,
                                                      estagio_id=atividade.estagioId,
                                                      fim_atividade=None).first()


atividade_estagio_dao = AtividadeEstagioDao(AtividadeEstagio)
