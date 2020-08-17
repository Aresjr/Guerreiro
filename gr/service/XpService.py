from app import db
from gr.dao.AtividadeDao import atividade_dao
from gr.dao.NivelHabilidadeDao import nivel_habilidade_dao
from gr.dao.UsuarioDao import usuario_dao
from gr.dao.XpDao import xp_dao


class XpService:

    def levelup_by_usuario(self, usuario):
        atividades = atividade_dao.get_xp_nao_contabilizados(usuario.id)
        xp_fator = usuario.setor.empresa.xpFator
        for atividade in atividades:
            xps = xp_dao.get_by_atividadeid(atividade.id)
            for xp in xps:

                # acumula o xp para o usuario
                xp_total_usuario = xp.valor
                while usuario.currentXp + xp_total_usuario > usuario.nextLevelXp:
                    usuario.level += 1
                    xp_total_usuario -= usuario.nextLevelXp
                    usuario.nextLevelXp = round(usuario.nextLevelXp * xp_fator)
                usuario.currentXp += xp_total_usuario  # xp que sobra

                # acumula o xp para o nivel de habilidade do usuario
                xp_total_habilidade = xp.valor
                nh = nivel_habilidade_dao.get_nivel_by_usuario_habilidade(usuario.id, xp.habilidadeId)
                if not nh:
                    nivel_habilidade_dao.insert(usuario.id, xp.habilidadeId)
                    nh = nivel_habilidade_dao.get_nivel_by_usuario_habilidade(usuario.id, xp.habilidadeId)
                while nh.currentXp + xp_total_habilidade > nh.nextLevelXp:
                    nh.level += 1
                    xp_total_habilidade -= nh.nextLevelXp
                    nh.nextLevelXp = round(nh.nextLevelXp * xp_fator)
                nh.currentXp += xp_total_habilidade  # xp que sobra
                nivel_habilidade_dao.update(nh)

            atividade.xpContabilizado = True
            # atividade_dao.update(atividade)
        usuario_dao.update(usuario)


xp_service = XpService()
