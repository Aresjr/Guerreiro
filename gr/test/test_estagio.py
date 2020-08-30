import pytest

from gr.dao.EstagioDao import estagio_dao
from gr.service.EstagioService import estagio_service

@pytest.fixture
def carga_estagios():
    todo = estagio_dao.get_by_titulo('TODO')
    todo.ordem = 1
    doing = estagio_dao.get_by_titulo('Doing')
    doing.ordem = 2
    testing = estagio_dao.get_by_titulo('Testing')
    testing.ordem = 3
    done = estagio_dao.get_by_titulo('Done')
    done.ordem = 4
    estagios = [todo, doing, testing, done]
    return estagios

def test_trocar_ordem_estagio_crescente(carga_estagios):

    todo = carga_estagios[0]
    doing = carga_estagios[1]
    testing = carga_estagios[2]
    done = carga_estagios[3]

    assert todo.ordem == 1
    assert doing.ordem == 2
    assert testing.ordem == 3
    assert done.ordem == 4

    estagio_service.alterar_ordem(doing.id, 4)

    assert todo.ordem == 1
    assert testing.ordem == 2
    assert done.ordem == 3
    assert doing.ordem == 4

def test_trocar_ordem_estagio_decrescente(carga_estagios):

    todo = carga_estagios[0]
    doing = carga_estagios[1]
    testing = carga_estagios[2]
    done = carga_estagios[3]

    assert todo.ordem == 1
    assert doing.ordem == 2
    assert testing.ordem == 3
    assert done.ordem == 4

    estagio_service.alterar_ordem(done.id, 2)

    assert todo.ordem == 1
    assert done.ordem == 2
    assert doing.ordem == 3
    assert testing.ordem == 4

def test_trocar_ordem_estagio_normal(carga_estagios):

    todo = carga_estagios[0]
    doing = carga_estagios[1]
    testing = carga_estagios[2]
    done = carga_estagios[3]

    assert todo.ordem == 1
    assert doing.ordem == 2
    assert testing.ordem == 3
    assert done.ordem == 4

    estagio_service.alterar_ordem(testing.id, 3)

    assert todo.ordem == 1
    assert doing.ordem == 2
    assert testing.ordem == 3
    assert done.ordem == 4
