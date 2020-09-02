import pytest

from app import app
from gr.dao.AtividadeDao import atividade_dao
from gr.dao.CargoDao import cargo_dao
from gr.dao.ConquistaDao import conquista_dao
from gr.dao.EmpresaDao import empresa_dao
from gr.dao.EstagioDao import estagio_dao
from gr.dao.HabilidadeDao import habilidade_dao
from gr.dao.NivelHabilidadeDao import nivel_habilidade_dao
from gr.dao.SetorDao import setor_dao
from gr.dao.TipoAtividadeDao import tipo_atividade_dao
from gr.dao.TipoConquistaDao import tipo_conquista_dao
from gr.dao.UsuarioDao import usuario_dao
from gr.dao.XpDao import xp_dao
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


@pytest.fixture
def carga():

    app.config.from_object("config.TestingConfig")

    # DELETA OS DADOS FISICAMENTE
    xp_dao.purge_all()
    atividade_dao.purge_all()
    conquista_dao.purge_all()
    tipo_conquista_dao.purge_all()
    nivel_habilidade_dao.purge_all()
    usuario_dao.purge_all()
    cargo_dao.purge_all()
    estagio_dao.purge_all()
    tipo_atividade_dao.purge_all()
    setor_dao.purge_all()
    empresa_dao.purge_all()
    habilidade_dao.purge_all()

    # EMPRESA
    empresa = Empresa(nome='Nemeia', xpFator=1.15, xpPrimeiroNivel=100, xpPorAtividade=12)
    empresa_dao.add(empresa)

    # SETOR
    setor = Setor(nome='Tecnologia', empresaId=empresa.id)
    setor_dao.add(setor)

    # CARGO
    cargo_prog_sr = Cargo(titulo='Programador Sênior')
    cargo_prog_pl = Cargo(titulo='Programador Pleno', cargoSuperiorId=cargo_prog_sr.id)
    cargo_prog_jr = Cargo(titulo='Programador Júnior', cargoSuperiorId=cargo_prog_pl.id)
    cargo_dao.add_all([cargo_prog_jr, cargo_prog_pl, cargo_prog_sr])

    # USUARIOS
    ares = Usuario(nome='Aristides Cândido Júnior', username='ares', email='ares@ares.dev.br', setorId=setor.id, cargoId=cargo_prog_sr.id)
    ares.set_password('aresroot')
    dante = Usuario(nome='Dante', username='dante', email='dante@ares.dev.br', setorId=setor.id)
    dante.set_password('danteroot')
    usuario_dao.add_all([ares, dante])

    # ESTAGIOS
    estagio1 = Estagio(titulo='TODO', ordem=1, empresaId=empresa.id, estagioInicial=True)
    estagio2 = Estagio(titulo='Doing', ordem=2, empresaId=empresa.id)
    estagio3 = Estagio(titulo='Testing', ordem=3, empresaId=empresa.id, estagioTeste=True)
    estagio4 = Estagio(titulo='Done', ordem=4, empresaId=empresa.id, estagioFinal=True)
    estagios = [estagio1, estagio2, estagio3, estagio4]
    estagio_dao.add_all(estagios)

    # ATIVIDADES
    ativ1 = Atividade(codigo='1', descricao='Desenvolver tela de Atividades', usuarioExecucaoId=ares.id, estagioId=estagio1.id)
    ativ2 = Atividade(codigo='Dois', descricao='Desenvolver tela de Apontamentos', usuarioExecucaoId=ares.id, estagioId=estagio1.id)
    ativ3 = Atividade(codigo='3-A', descricao='Modelagem de Dados', usuarioExecucaoId=ares.id, estagioId=estagio1.id)
    ativ4 = Atividade(codigo=None, descricao='Quarta Atividade', usuarioExecucaoId=ares.id, estagioId=estagio1.id)
    ativ5 = Atividade(codigo='5', descricao='Quinta Atividade', usuarioExecucaoId=ares.id, estagioId=estagio1.id)
    ativ6 = Atividade(codigo='OS-123', descricao='Sexta Atividade', usuarioExecucaoId=ares.id, estagioId=estagio1.id)
    atividades = [ativ1, ativ2, ativ3, ativ4, ativ5, ativ6]
    atividade_dao.add_all(atividades)

    # TIPO CONQUISTA
    tipo_conq1 = TipoConquista(titulo='Level Up!', descricao='Subiu para o Nível {}', destaque=True, icone='levelup')
    tipo_conq2 = TipoConquista(titulo='Level Up de Habilidade', descricao='Habilidade {} subiu para o Nível {}', destaque=False, icone='skillup')
    tipo_conqs = [tipo_conq1, tipo_conq2]
    tipo_conquista_dao.add_all(tipo_conqs)

    # HABILIDADES
    hab_prog = Habilidade(descricao='Programação')
    hab_python = Habilidade(descricao='Python', habPaiId=hab_prog.id)
    hab_js = Habilidade(descricao='Javascript', habPaiId=hab_prog.id)
    hab_java = Habilidade(descricao='Java', habPaiId=hab_prog.id)

    hab_db = Habilidade(descricao='Banco de Dados')
    hab_postgresql = Habilidade(descricao='PostgreSQL', habPaiId=hab_db.id)
    hab_oracle = Habilidade(descricao='Oracle', habPaiId=hab_db.id)
    hab_mongodb = Habilidade(descricao='MongoDB', habPaiId=hab_db.id)

    hab_frontend = Habilidade(descricao='Front End')
    hab_css = Habilidade(descricao='HTML/CSS', habPaiId=hab_frontend.id)
    hab_angular = Habilidade(descricao='Angular', habPaiId=hab_frontend.id)
    hab_vue = Habilidade(descricao='Vue', habPaiId=hab_frontend.id)

    hab_engsoft = Habilidade(descricao='Enenharia de Software')
    hab_mod_dados = Habilidade(descricao='Modelagem de Dados', habPaiId=hab_engsoft.id)

    hab_analise = Habilidade(descricao='Análise')
    hab_an_sis = Habilidade(descricao='Análise de Sistemas', habPaiId=hab_analise.id)
    hab_an_neg = Habilidade(descricao='Análise de Negócio', habPaiId=hab_analise.id)

    hab_ia = Habilidade(descricao='Inteligência Aritificial')
    hab_ml = Habilidade(descricao='Machine Learning', habPaiId=hab_ia.id)
    hab_nlp = Habilidade(descricao='Natural Language Processing', habPaiId=hab_ia.id)

    hab_ds = Habilidade(descricao='Ciência de Dados')
    hab_ds_da = Habilidade(descricao='Análise de Dados', habPaiId=hab_ds.id)
    hab_ds_etl = Habilidade(descricao='ETL', habPaiId=hab_ds.id)

    habilidades = [hab_prog, hab_python, hab_js, hab_java, hab_db, hab_postgresql, hab_mongodb, hab_oracle,
                   hab_frontend, hab_css, hab_vue, hab_angular, hab_engsoft, hab_mod_dados, hab_analise,
                   hab_an_neg, hab_an_sis, hab_ia, hab_ml, hab_nlp, hab_ds, hab_ds_da, hab_ds_etl]
    habilidade_dao.add_all(habilidades)

    # TIPO ATIVIDADE
    ta1 = TipoAtividade(descricao='Desenvolvimento Tela')
    ta2 = TipoAtividade(descricao='Desenvolvimento API')
    ta3 = TipoAtividade(descricao='Estrutura de Dados')
    ta4 = TipoAtividade(descricao='Desenvolvimento do Mestre')
    tas = [ta1, ta2, ta3, ta4]
    tipo_atividade_dao.add_all(tas)

    # XP
    xp1 = Xp(atividadeId=ativ1.id, habilidadeId=hab_python.id, valor=40)
    xp2 = Xp(atividadeId=ativ1.id, habilidadeId=hab_js.id, valor=40)
    xp3 = Xp(atividadeId=ativ1.id, habilidadeId=hab_css.id, valor=20)
    xp4 = Xp(atividadeId=ativ1.id, habilidadeId=hab_python.id, valor=20)
    xp5 = Xp(atividadeId=ativ1.id, habilidadeId=hab_an_neg.id, valor=40)
    xp6 = Xp(atividadeId=ativ1.id, habilidadeId=hab_python.id, valor=40)
    xp7 = Xp(atividadeId=ativ1.id, habilidadeId=hab_js.id, valor=20)
    xp8 = Xp(atividadeId=ativ1.id, habilidadeId=hab_an_sis.id, valor=20)
    xp9 = Xp(atividadeId=ativ2.id, habilidadeId=hab_angular.id, valor=40)
    xp10 = Xp(atividadeId=ativ2.id, habilidadeId=hab_java.id, valor=40)
    xp11 = Xp(atividadeId=ativ2.id, habilidadeId=hab_js.id, valor=20)
    xp12 = Xp(atividadeId=ativ2.id, habilidadeId=hab_an_sis.id, valor=20)
    xp13 = Xp(atividadeId=ativ2.id, habilidadeId=hab_angular.id, valor=40)
    xp14 = Xp(atividadeId=ativ2.id, habilidadeId=hab_java.id, valor=40)
    xp15 = Xp(atividadeId=ativ3.id, habilidadeId=hab_js.id, valor=20)
    xp16 = Xp(atividadeId=ativ3.id, habilidadeId=hab_an_sis.id, valor=20)
    xp17 = Xp(atividadeId=ativ3.id, habilidadeId=hab_angular.id, valor=40)
    xp18 = Xp(atividadeId=ativ3.id, habilidadeId=hab_java.id, valor=40)
    xp19 = Xp(atividadeId=ativ3.id, habilidadeId=hab_js.id, valor=20)
    xp20 = Xp(atividadeId=ativ3.id, habilidadeId=hab_an_sis.id, valor=20)
    xps = [xp1, xp2, xp3, xp4, xp5, xp6, xp7, xp8, xp9, xp10, xp11, xp12, xp13, xp14, xp15, xp16, xp17, xp18, xp19, xp20]
    xp_dao.add_all(xps)

    return habilidades, tipo_conqs, atividades, tas, xps, estagios

def test_carga(carga):
    assert True

