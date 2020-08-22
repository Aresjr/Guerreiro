from gr.dao.EstagioDao import estagio_dao


class EstagioService:

    def get_quadro_by_usuario(self, usuario):

        estagios = estagio_dao.get_by_empresa(usuario.setor.empresa.id)
        estagios_json = []
        for estagio in estagios:

            itens = []
            for atividade in estagio.atividades:
                itens.append({
                    'id': str(atividade.id),
                    'title': atividade.codigo,
                    'descricao': atividade.descricao,
                    'estagio': estagio.id,
                    'executor': atividade.usuarioExecucao.username
                })

            estagios_json.append({
                'id': str(estagio.id),
                'title': estagio.titulo,
                'item': itens,
                'dragTo': ['1', '2', '3', '4']
            })

        return estagios_json

    def alterar_ordem(self, estagio_id, ordem_nova):

        estagio = estagio_dao.get(estagio_id)
        ordem_anterior = False
        if estagio.ordem < ordem_nova:
            ordem_anterior = True

        estagios = estagio_dao.get_by_empresa_ordem(estagio.empresa.id, estagio.ordem if ordem_anterior else ordem_nova, ordem_nova if ordem_anterior else estagio.ordem)

        for estagio in estagios:
            if estagio.id == estagio_id:
                estagio.ordem = ordem_nova
            else:
                if ordem_anterior:
                    estagio.ordem -= 1
                else:
                    estagio.ordem += 1
        estagio_dao.update_all(estagios)


estagio_service = EstagioService()
