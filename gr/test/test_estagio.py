from gr.dao.EstagioDao import estagio_dao
from gr.service.EstagioService import estagio_service


def test_trocar_ordem_estagio_crescente():

    todo = estagio_dao.get(1)
    todo.ordem = 1
    estagio_dao.update(todo)
    doing = estagio_dao.get(2)
    doing.ordem = 2
    estagio_dao.update(doing)
    testing = estagio_dao.get(3)
    testing.ordem = 3
    estagio_dao.update(testing)
    done = estagio_dao.get(4)
    done.ordem = 4
    estagio_dao.update(done)

    assert todo.ordem == 1
    assert doing.ordem == 2
    assert testing.ordem == 3
    assert done.ordem == 4

    estagio_service.alterar_ordem(doing.id, 4)

    assert todo.ordem == 1
    assert testing.ordem == 2
    assert done.ordem == 3
    assert doing.ordem == 4

def test_trocar_ordem_estagio_decrescente():

    todo = estagio_dao.get(1)
    todo.ordem = 1
    estagio_dao.update(todo)
    doing = estagio_dao.get(2)
    doing.ordem = 2
    estagio_dao.update(doing)
    testing = estagio_dao.get(3)
    testing.ordem = 3
    estagio_dao.update(testing)
    done = estagio_dao.get(4)
    done.ordem = 4
    estagio_dao.update(done)

    assert todo.ordem == 1
    assert doing.ordem == 2
    assert testing.ordem == 3
    assert done.ordem == 4

    estagio_service.alterar_ordem(done.id, 2)

    assert todo.ordem == 1
    assert done.ordem == 2
    assert doing.ordem == 3
    assert testing.ordem == 4
