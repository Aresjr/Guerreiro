from gr.dao.NivelHabilidadeDao import nivel_habilidade_dao


class NivelHabilidadeService:

    def add_xp(self, usuario, nh, total_xp):
        xp_fator = usuario.setor.empresa.xpFator
        while nh.currentXp + total_xp >= nh.nextLevelXp:
            nh.level += 1
            total_xp -= nh.nextLevelXp
            nh.nextLevelXp = round(nh.nextLevelXp * xp_fator)
        nh.currentXp += total_xp  # total_xp que sobra
        return nivel_habilidade_dao.upsert(nh)

    def get_nh_usuario(self, usuarioid):
        nhs = nivel_habilidade_dao.get_by_usuario(usuarioid)
        v_nhs = {}
        for nh in nhs:
            width = int(100 / nh.nextLevelXp * nh.currentXp)
            if nh.habilidade.habPaiId is None:
                v_nhs[nh.habilidade.id] = vars(nh)
                v_nhs[nh.habilidade.id]['width'] = width
                v_nhs[nh.habilidade.id]['habFilho'] = []
                v_nhs[nh.habilidade.id]['habilidade'] = vars(nh.habilidade)
            else:
                hab_filho = vars(nh)
                hab_pai_id = nh.habilidade.habPaiId
                hab_filho['habilidade'] = vars(nh.habilidade)
                hab_filho['width'] = width
                v_nhs[hab_pai_id]['habFilho'].append(hab_filho)
        return v_nhs


nivel_habilidade_service = NivelHabilidadeService()
