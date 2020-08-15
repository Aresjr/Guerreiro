from datetime import datetime

from app import db
from gr.dao.AtividadeDao import atividade_dao
from gr.dao.EstagioDao import estagio_dao
from gr.model.manyToMany.AtividadeEstagio import AtividadeEstagio


class AtividadeService:

    def get_quadro_by_usuario(self, usuario, atividadeid, estagioid):
        atividade = atividade_dao.get_by_id(atividadeid)
        atividade_estagio = db.session.query(AtividadeEstagio).filter_by(atividade_id=atividadeid,
                                                                         estagio_id=atividade.estagioId,
                                                                         fim_atividade=None).first()

        if atividade_estagio:
            atividade_estagio_update = AtividadeEstagio.update().where(AtividadeEstagio.c.atividade_id == atividadeid) \
                .where(AtividadeEstagio.c.estagio_id == atividade.estagioId) \
                .where(AtividadeEstagio.c.fim_atividade == None).values(fim_atividade=datetime.now())
            db.session.execute(atividade_estagio_update)

        atividade.estagioId = estagioid
        db.session.add(atividade)

        atividade_estagio = AtividadeEstagio.insert().values(atividade_id=atividadeid, estagio_id=estagioid,
                                                             usuario_id=usuario.id, incio_atividade=datetime.now())
        db.session.execute(atividade_estagio)
        db.session.commit()

atividade_service = AtividadeService()
