from datetime import datetime

from app import db
from gr.model.manyToMany.AtividadeEstagio import AtividadeEstagio


class AtividadeEstagioDao:
    def __init__(self, model):
        self.model = model

    def get_by_id(self, atividade, atividadeid):
        return db.session.query(self.model).filter_by(atividade_id=atividadeid,
                                                      estagio_id=atividade.estagioId,
                                                      fim_atividade=None).first()

    def get_by_atividade_estagio(self, atividadeid, estagioid):
        return db.session.query(self.model).filter_by(atividade_id=atividadeid,
                                                      estagio_id=estagioid,
                                                      fim_atividade=None).first()

    def finalizar_atividade_estagio(self, atividadeid, estagioid):
        return db.session.execute(
            self.model.update().where(self.model.c.atividade_id == atividadeid) \
                .where(self.model.c.estagio_id == estagioid) \
                .where(self.model.c.fim_atividade == None).values(fim_atividade=datetime.now())
        )

    def inserir(self, atividadeid, estagioid, usuarioid):
        db.session.execute(
            self.model.insert().values(atividade_id=atividadeid, estagio_id=estagioid,
                                       usuario_id=usuarioid, incio_atividade=datetime.now())
        )
        return db.session.commit()


atividade_estagio_dao = AtividadeEstagioDao(AtividadeEstagio)
