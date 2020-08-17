from gr.dao.AtividadeDao import atividade_dao
from gr.dao.AtividadeEstagioDao import atividade_estagio_dao
from gr.dao.NivelHabilidadeDao import nivel_habilidade_dao
from gr.dao.UsuarioDao import usuario_dao
from gr.dao.XpDao import xp_dao
from gr.service.NivelHabilidadeService import nivel_habilidade_service
from gr.service.UsuarioService import usuario_service


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

    def contabiliza_xp_usuario(selfself, usuario):
        atividades = atividade_dao.get_xp_nao_contabilizados(usuario.id)
        for atividade in atividades:
            xps = xp_dao.get_by_atividadeid(atividade.id)
            for xp in xps:
                print(xp.valor)
                usuario_service.add_xp(usuario, xp.valor)
                print(xp.valor)

                # acumula o total_xp total da habilidade pai atual (programacao, analise de dados, bd, ciencia de dados, etc)
                # xp_total_habilidade_pai = xp.valor
                # nh = nivel_habilidade_dao.get_or_insert_nh(usuario.id, xp.habilidadeId)
                # nivel_habilidade_service.add_xp(usuario, nh, xp.valor)

                # acumula o total_xp para o nivel de habilidade do usuario
                # xp_total_habilidade = xp.valor
                nh = nivel_habilidade_dao.get_or_insert_nh(usuario.id, xp.habilidadeId)
                print(nh.currentXp)
                nivel_habilidade_service.add_xp(usuario, nh, xp.valor)
                print(nh.currentXp)

            atividade.xpContabilizado = True
            atividade_dao.update(atividade)
        usuario_dao.update(usuario)


atividade_service = AtividadeService()
