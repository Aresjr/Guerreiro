from datetime import datetime

import pytest
# noinspection PyUnresolvedReferences
from app import app, db
from gr.model.atividades.Atividade import Atividade
from gr.model.atividades.Estagio import Estagio
from gr.model.atividades.TipoAtividade import TipoAtividade
from gr.model.empresa.Empresa import Empresa
from gr.model.empresa.Setor import Setor
from gr.model.usuario.Habilidade import Habilidade
from gr.model.usuario.TipoConquista import TipoConquista
from gr.model.usuario.Usuario import Usuario


def test_models():
    # assert usuario.setor.empresa.nome == 'NemeIA'
    assert 1 == 1

@pytest.fixture
def carga_inicial():
    empresa = Empresa(id=1, nome='NemeIA', xpFator=0.15, xpPrimeiroNivel=100, xpPorAtividade=12)
    if Empresa.query.count() == 0:
        db.session.add(empresa)

    setor = Setor(empresa=empresa)
    if Setor.query.count() == 0:
        db.session.add(setor)

    ares = Usuario(id=1, nome='Aristides Cândido Júnior', username='ares', email='ares@ares.dev.br')
    ares.set_password('aresroot')
    if not Usuario.query.filter(Usuario.username == 'ares').first():
        db.session.add(ares)

    dante = Usuario(id=2, nome='Dante', username='dante', email='dante@ares.dev.br')
    dante.set_password('danteroot')
    if not Usuario.query.filter(Usuario.username == 'dante').first():
        db.session.add(dante)

    ativ1 = Atividade(id=1, codigo='1', descricao='Desenvolver tela de Atividades', usuarioExecucao=ares.id)
    ativ2 = Atividade(id=2, codigo='Dois', descricao='Desenvolver tela de Apontamentos', usuarioExecucao=ares.id)
    ativ3 = Atividade(id=3, codigo='3-A', descricao='Modelagem de Dados', usuarioExecucao=ares.id)
    ativ4 = Atividade(id=4, codigo=None, descricao='Quarta Atividade', usuarioExecucao=ares.id)
    ativ5 = Atividade(id=5, codigo='5', descricao='Quinta Atividade', usuarioExecucao=ares.id)
    ativ6 = Atividade(id=6, codigo='OS-123', descricao='Sexta Atividade', usuarioExecucao=ares.id)
    atividades = [ativ1, ativ2, ativ3, ativ4, ativ5, ativ6]
    if Atividade.query.count() == 0:
        db.session.add_all(atividades)

    estagio1 = Estagio(id=1, titulo='TO DO', ordem=1, estagioInicial=True)
    estagio2 = Estagio(id=2, titulo='Doing', ordem=2)
    estagio3 = Estagio(id=3, titulo='Testing', ordem=3, estagioTeste=True)
    estagio4 = Estagio(id=4, titulo='Done', ordem=4, estagioFinal=True)
    if Estagio.query.count() == 0:
        db.session.add_all([estagio1, estagio2, estagio3, estagio4])

    tipo_conq1 = TipoConquista(id=1, titulo='Level Up!', destaque=True, icone='levelup')
    tipo_conq2 = TipoConquista(id=2, titulo='Habilidade Subiu de Nível', destaque=False, icone='skillup')
    if TipoConquista.query.count() == 0:
        db.session.add_all([tipo_conq1, tipo_conq2])

    hab_prog = Habilidade(id=1, descricao='Programação')
    hab_python = Habilidade(id=2, descricao='Python', habPaiId=hab_prog.id)
    hab_js = Habilidade(id=3, descricao='Javascript', habPaiId=hab_prog.id)
    hab_java = Habilidade(id=4, descricao='Java', habPaiId=hab_prog.id)

    hab_db = Habilidade(id=5, descricao='Banco de Dados')
    hab_postgresql = Habilidade(id=6, descricao='PostgreSQL', habPaiId=hab_db.id)
    hab_oracle = Habilidade(id=7, descricao='Oracle', habPaiId=hab_db.id)
    hab_mongodb = Habilidade(id=8, descricao='MongoDB', habPaiId=hab_db.id)

    hab_frontend = Habilidade(id=9, descricao='Front End')
    hab_css = Habilidade(id=10, descricao='HTML/CSS', habPaiId=hab_frontend.id)
    hab_angular = Habilidade(id=11, descricao='Angular', habPaiId=hab_frontend.id)
    hab_vue = Habilidade(id=12, descricao='Vue', habPaiId=hab_frontend.id)

    hab_engsoft = Habilidade(id=13, descricao='Enenharia de Software')
    hab_mod_dados = Habilidade(id=14, descricao='Modelagem de Dados', habPaiId=hab_engsoft.id)

    hab_analise = Habilidade(id=15, descricao='Análise')
    hab_an_sis = Habilidade(id=16, descricao='Análise de Sistemas', habPaiId=hab_analise.id)
    hab_an_neg = Habilidade(id=17, descricao='Análise de Negócio', habPaiId=hab_analise.id)

    hab_ia = Habilidade(id=18, descricao='Inteligência Aritificial')
    hab_ml = Habilidade(id=19, descricao='Machine Learning', habPaiId=hab_ia.id)
    hab_nlp = Habilidade(id=20, descricao='Natural Language Processing', habPaiId=hab_ia.id)

    hab_ds = Habilidade(id=21, descricao='Ciência de Dados')
    hab_ds_da = Habilidade(id=22, descricao='Análise de Dados', habPaiId=hab_ia.id)
    hab_ds_etl = Habilidade(id=23, descricao='ETL', habPaiId=hab_ia.id)

    habilidades = [hab_prog, hab_python, hab_js, hab_java, hab_db, hab_postgresql, hab_mongodb, hab_oracle,
                   hab_frontend, hab_css, hab_vue, hab_angular, hab_engsoft, hab_mod_dados, hab_analise,
                   hab_an_neg, hab_an_sis, hab_ia, hab_ml, hab_nlp, hab_ds, hab_ds_da, hab_ds_etl]
    if Habilidade.query.count() == 0:
        db.session.add_all(habilidades)

    db.session.commit()
