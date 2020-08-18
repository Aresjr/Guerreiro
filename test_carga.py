import pytest
from app import db
from gr.model.atividades.Atividade import Atividade
from gr.model.atividades.Estagio import Estagio
from gr.model.atividades.TipoAtividade import TipoAtividade
from gr.model.empresa.Empresa import Empresa
from gr.model.empresa.Setor import Setor
from gr.model.usuario.Habilidade import Habilidade
from gr.model.usuario.TipoConquista import TipoConquista
from gr.model.usuario.Usuario import Usuario
from gr.model.usuario.Xp import Xp
from gr.model.vaga.Cargo import Cargo


def test_carga(carga):
    assert carga


@pytest.fixture
def carga():

    # EMPRESA
    empresa = Empresa(id=1, nome='Nemeia', xpFator=1.15, xpPrimeiroNivel=100, xpPorAtividade=12)
    if Empresa.query.count() == 0:
        db.session.add(empresa)

    # SETOR
    setor = Setor(id=1, nome='Tecnologia', empresaId=empresa.id)
    if Setor.query.count() == 0:
        db.session.add(setor)

    # CARGO
    cargo_prog_sr = Cargo(id=1, titulo='Programador Sênior')
    cargo_prog_pl = Cargo(id=2, titulo='Programador Pleno', cargoSuperiorId=cargo_prog_sr.id)
    cargo_prog_jr = Cargo(id=3, titulo='Programador Júnior', cargoSuperiorId=cargo_prog_pl.id)
    if Cargo.query.count() == 0:
        db.session.add_all([cargo_prog_jr, cargo_prog_pl, cargo_prog_sr])
        db.session.commit()

    # USUARIOS
    ares = Usuario(id=1, nome='Aristides Cândido Júnior', username='ares', email='ares@ares.dev.br', setorId=setor.id, cargoId=cargo_prog_sr.id)
    ares.set_password('aresroot')
    dante = Usuario(id=2, nome='Dante', username='dante', email='dante@ares.dev.br', setorId=setor.id)
    dante.set_password('danteroot')
    if Usuario.query.count() == 0:
        db.session.add_all([ares, dante])

    # ESTAGIOS
    estagio1 = Estagio(id=1, titulo='TO DO', ordem=1, empresaId=empresa.id, estagioInicial=True)
    estagio2 = Estagio(id=2, titulo='Doing', ordem=2, empresaId=empresa.id)
    estagio3 = Estagio(id=3, titulo='Testing', ordem=3, empresaId=empresa.id, estagioTeste=True)
    estagio4 = Estagio(id=4, titulo='Done', ordem=4, empresaId=empresa.id, estagioFinal=True)
    estagios = [estagio1, estagio2, estagio3, estagio4]
    if Estagio.query.count() == 0:
        db.session.add_all(estagios)

    # ATIVIDADES
    ativ1 = Atividade(id=1, codigo='1', descricao='Desenvolver tela de Atividades', usuarioExecucaoId=ares.id, estagioId=estagio1.id)
    ativ2 = Atividade(id=2, codigo='Dois', descricao='Desenvolver tela de Apontamentos', usuarioExecucaoId=ares.id, estagioId=estagio1.id)
    ativ3 = Atividade(id=3, codigo='3-A', descricao='Modelagem de Dados', usuarioExecucaoId=ares.id, estagioId=estagio1.id)
    ativ4 = Atividade(id=4, codigo=None, descricao='Quarta Atividade', usuarioExecucaoId=ares.id, estagioId=estagio1.id)
    ativ5 = Atividade(id=5, codigo='5', descricao='Quinta Atividade', usuarioExecucaoId=ares.id, estagioId=estagio1.id)
    ativ6 = Atividade(id=6, codigo='OS-123', descricao='Sexta Atividade', usuarioExecucaoId=ares.id, estagioId=estagio1.id)
    atividades = [ativ1, ativ2, ativ3, ativ4, ativ5, ativ6]
    if Atividade.query.count() == 0:
        db.session.add_all(atividades)

    # TIPO CONQUISTA
    tipo_conq1 = TipoConquista(id=1, titulo='Level Up!', destaque=True, icone='levelup')
    tipo_conq2 = TipoConquista(id=2, titulo='Habilidade Subiu de Nível', destaque=False, icone='skillup')
    tipo_conqs = [tipo_conq1, tipo_conq2]
    if TipoConquista.query.count() == 0:
        db.session.add_all(tipo_conqs)

    # HABILIDADES
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
    hab_ds_da = Habilidade(id=22, descricao='Análise de Dados', habPaiId=hab_ds.id)
    hab_ds_etl = Habilidade(id=23, descricao='ETL', habPaiId=hab_ds.id)

    habilidades = [hab_prog, hab_python, hab_js, hab_java, hab_db, hab_postgresql, hab_mongodb, hab_oracle,
                   hab_frontend, hab_css, hab_vue, hab_angular, hab_engsoft, hab_mod_dados, hab_analise,
                   hab_an_neg, hab_an_sis, hab_ia, hab_ml, hab_nlp, hab_ds, hab_ds_da, hab_ds_etl]
    if Habilidade.query.count() == 0:
        db.session.add_all(habilidades)

    # TIPO ATIVIDADE
    ta1 = TipoAtividade(id=1, descricao='Desenvolvimento Tela')
    ta2 = TipoAtividade(id=2, descricao='Desenvolvimento API')
    ta3 = TipoAtividade(id=3, descricao='Estrutura de Dados')
    ta4 = TipoAtividade(id=4, descricao='Desenvolvimento do Mestre')
    tas = [ta1, ta2, ta3, ta4]
    if TipoAtividade.query.count() == 0:
        db.session.add_all(tas)

    # XP
    xp1 = Xp(id=1, atividadeId=ativ1.id, habilidadeId=hab_python.id, valor=40)
    xp2 = Xp(id=2, atividadeId=ativ1.id, habilidadeId=hab_js.id, valor=40)
    xp3 = Xp(id=3, atividadeId=ativ1.id, habilidadeId=hab_css.id, valor=20)
    xp4 = Xp(id=4, atividadeId=ativ1.id, habilidadeId=hab_python.id, valor=20)
    xp5 = Xp(id=5, atividadeId=ativ1.id, habilidadeId=hab_an_neg.id, valor=40)
    xp6 = Xp(id=6, atividadeId=ativ1.id, habilidadeId=hab_python.id, valor=40)
    xp7 = Xp(id=7, atividadeId=ativ1.id, habilidadeId=hab_js.id, valor=20)
    xp8 = Xp(id=8, atividadeId=ativ1.id, habilidadeId=hab_an_sis.id, valor=20)
    xp9 = Xp(id=9, atividadeId=ativ2.id, habilidadeId=hab_angular.id, valor=40)
    xp10 = Xp(id=10, atividadeId=ativ2.id, habilidadeId=hab_java.id, valor=40)
    xp11 = Xp(id=11, atividadeId=ativ2.id, habilidadeId=hab_js.id, valor=20)
    xp12 = Xp(id=12, atividadeId=ativ2.id, habilidadeId=hab_an_sis.id, valor=20)
    xp13 = Xp(id=13, atividadeId=ativ2.id, habilidadeId=hab_angular.id, valor=40)
    xp14 = Xp(id=14, atividadeId=ativ2.id, habilidadeId=hab_java.id, valor=40)
    xp15 = Xp(id=15, atividadeId=ativ3.id, habilidadeId=hab_js.id, valor=20)
    xp16 = Xp(id=16, atividadeId=ativ3.id, habilidadeId=hab_an_sis.id, valor=20)
    xp17 = Xp(id=17, atividadeId=ativ3.id, habilidadeId=hab_angular.id, valor=40)
    xp18 = Xp(id=18, atividadeId=ativ3.id, habilidadeId=hab_java.id, valor=40)
    xp19 = Xp(id=19, atividadeId=ativ3.id, habilidadeId=hab_js.id, valor=20)
    xp20 = Xp(id=20, atividadeId=ativ3.id, habilidadeId=hab_an_sis.id, valor=20)
    xps = [xp1, xp2, xp3, xp4, xp5, xp6, xp7, xp8, xp9, xp10, xp11, xp12, xp13, xp14, xp15, xp16, xp17, xp18, xp19, xp20]
    if Xp.query.count() == 0:
        db.session.add_all(xps)

    db.session.commit()
    return habilidades, tipo_conqs, atividades, tas, xps
