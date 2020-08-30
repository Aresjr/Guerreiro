from gr.dao.ConquistaDao import conquista_dao
from gr.dao.NivelHabilidadeDao import nivel_habilidade_dao
from gr.dao.UsuarioDao import usuario_dao
from gr.service.AtividadeService import atividade_service
# noinspection PyUnresolvedReferences
from gr.test.test_carga import carga


def test_levelup(carga):
    usuario = usuario_dao.get_by_username('ares')

    # delete fisico
    nivel_habilidade_dao.purge_all()
    conquista_dao.purge_all()
    atividade_service.contabiliza_xp_usuario(usuario)

    assert usuario.level == 5
    assert usuario.nextLevelXp == 175
    assert usuario.currentXp == 101
    assert len(conquista_dao.get_all()) == 4
