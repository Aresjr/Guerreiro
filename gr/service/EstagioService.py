from gr.dao.EstagioDao import estagio_dao


class EstagioService:

    def get_quadro_by_usuario(self, usuario):

        estagios = estagio_dao.get_by_empresa(usuario.setor.empresa.id)
        estagios_json = []
        for estagio in estagios:

            itens = []
            for atividade in estagio.atividades:
                itens.append({
                    'title': atividade.codigo,
                    'descricao': atividade.descricao,
                    'executor': 'executor: ' + atividade.usuarioExecucao.username,
                    'id': str(atividade.id)
                })

            estagios_json.append({
                'id': str(estagio.id),
                'title': estagio.titulo,
                'class': 'kb-info',
                'item': itens,
                'dragTo': ['1', '2', '3', '4']
            })

        return estagios_json


estagio_service = EstagioService()
