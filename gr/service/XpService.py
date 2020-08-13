from gr.dao.AtividadeDao import atividade_dao
from gr.dao.XpDao import xp_dao


class XpService:
    def levelup_by_usuario(self, usuario):
        atividades = atividade_dao.get_by_userid(usuario.id)
        xp_fator = usuario.setor.empresa.xpFator
        for atividade in atividades:
            xps = xp_dao.get_by_atividadeid(atividade.id)
            for xp in xps:
                xp_total = xp.valor
                while usuario.currentXp + xp_total > usuario.nextLevelXp:
                    usuario.level += 1
                    xp_total = xp_total - usuario.nextLevelXp
                    usuario.nextLevelXp = round(usuario.nextLevelXp * xp_fator)
                usuario.currentXp += xp_total
            atividade.xpContabilizado = True

    # def levelup_by_atividade(self, atividade, usuario):



xp_service = XpService()
