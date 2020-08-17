from gr.dao.AtividadeDao import atividade_dao
from gr.dao.AtividadeEstagioDao import atividade_estagio_dao


class NivelHabilidadeService:

    def iniciar_atividade(self, usuarioid, atividadeid, estagioid):
        atividade = atividade_dao.get_by_id(atividadeid)

        # finaliza atividade estagio anterior
        estagio_anterior = atividade.estagioId
        atividade_estagio_dao.finalizar_atividade_estagio(atividadeid, estagio_anterior)

        # atualiza estagio atual
        atividade.estagioId = estagioid
        atividade_dao.update(atividade)
        atividade_estagio_dao.inserir(atividadeid, estagioid, usuarioid)


nivel_habilidade_service = NivelHabilidadeService()
