from gr.dao.AtividadeDao import atividade_dao
from gr.dao.NivelHabilidadeDao import nivel_habilidade_dao
from gr.dao.UsuarioDao import usuario_dao
from gr.service.AtividadeService import atividade_service


def test_levelup():
    usuario = usuario_dao.get_by_username('ares')

    atividades = atividade_dao.get_all()
    for atividade in atividades:
        # marcar para ser contabilizado
        atividade.xpContabilizado = False
        atividade.dataContabilizacao = None
        atividade_dao.update(atividade)

    # delete fisicamente todos os niveis das habilidades
    nivel_habilidade_dao.purge_all()

    # marca como novo para contabilizar o xp do zero
    usuario.level = 1
    usuario.currentXp = 0
    usuario.nextLevelXp = 100
    usuario.setor.empresa.xpFator = 1.15
    atividade_service.contabiliza_xp_usuario(usuario)

    assert usuario.level == 5
    assert usuario.nextLevelXp == 175
    assert usuario.currentXp == 101
