from gr.dao.AtividadeDao import atividade_dao
from gr.dao.AtividadeEstagioDao import atividade_estagio_dao


class AtividadeService:

    def iniciar_atividade(self, usuarioid, atividadeid, estagioid):
        atividade = atividade_dao.get_by_id(atividadeid)
        estagio_anterior = atividade.estagioId

        if estagioid != estagio_anterior:
            # finaliza atividade estagio anterior
            atividade_estagio_dao.finalizar_atividade_estagio(atividadeid, estagio_anterior)

            # atualiza estagio atual
            atividade.estagioId = estagioid
            atividade_dao.update(atividade)

            atividade_estagio_dao.inserir(atividadeid, estagioid, usuarioid)


atividade_service = AtividadeService()
