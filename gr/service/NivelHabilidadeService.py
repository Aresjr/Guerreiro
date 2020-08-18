from gr.dao.NivelHabilidadeDao import nivel_habilidade_dao


class NivelHabilidadeService:

    def add_xp(self, usuario, nh, total_xp):
        xp_fator = usuario.setor.empresa.xpFator
        while nh.currentXp + total_xp >= nh.nextLevelXp:
            nh.level += 1
            total_xp -= nh.nextLevelXp
            nh.nextLevelXp = round(nh.nextLevelXp * xp_fator)
        nh.currentXp += total_xp  # total_xp que sobra
        return nivel_habilidade_dao.update(nh)


nivel_habilidade_service = NivelHabilidadeService()
