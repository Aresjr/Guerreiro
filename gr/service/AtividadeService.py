from gr.dao.AtividadeDao import atividade_dao
from gr.dao.AtividadeEstagioDao import atividade_estagio_dao
from gr.dao.NivelHabilidadeDao import nivel_habilidade_dao
from gr.dao.UsuarioDao import usuario_dao
from gr.dao.XpDao import xp_dao
from gr.model.atividades.Atividade import Atividade
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

    def contabiliza_xp_usuario(self, usuario):
        atividades = atividade_dao.get_xp_nao_contabilizados(usuario.id)
        for atividade in atividades:
            self.contabiliza_xp_atividade(usuario, atividade)
        usuario_dao.update(usuario)

    def contabiliza_xp_atividade(self, usuario, atividade):
        xps = xp_dao.get_by_atividadeid(atividade.id)
        print(atividade.id)
        print(xps)
        for xp in xps:
            self.contabiliza_xp(usuario, xp)
        atividade.xpContabilizado = True
        atividade_dao.update(atividade)

    def contabiliza_xp(self, usuario, xp):
        usuario_service.add_xp(usuario, xp.valor)

        # acumula o total_xp para o nivel de habilidade do usuario
        nh = nivel_habilidade_dao.get_or_insert_nh(usuario.id, xp.habilidadeId)
        nivel_habilidade_service.add_xp(usuario, nh, xp.valor)

        # acumula o total_xp para o nivel pai da habilidade
        if nh.habilidade.habPaiId:
            nh_pai = nivel_habilidade_dao.get_or_insert_nh(usuario.id, nh.habilidade.habPaiId)
            nivel_habilidade_service.add_xp(usuario, nh_pai, xp.valor)

    def add_atividade(self, titulo, descricao, usuario_execucao, usuario_criacao):
        Atividade(titulo=titulo, descricao=descricao, usuarioExecucaoId=usuario_execucao, usuarioCriacao=usuario_criacao)
        atividade_dao.add()

atividade_service = AtividadeService()
