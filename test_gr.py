import pytest

# noinspection PyUnresolvedReferences
from app import app

from gr.model.empresa.Empresa import Empresa
from gr.model.empresa.Setor import Setor
from gr.model.usuario.Usuario import Usuario


@pytest.fixture
def empresa():
    return Empresa(xpFator=0.15, xpValorBase=100, nome='NemeIA')


@pytest.fixture
def setor(empresa):
    return Setor(empresa=empresa)


@pytest.fixture
def usuario(setor):
    return Usuario(id=1, setor=setor, setorId=setor.id)


def test_levelup(usuario):
    assert usuario.setor.empresa.nome == 'NemeIA'
