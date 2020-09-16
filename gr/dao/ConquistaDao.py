from gr.dao.BaseDao import BaseDao
from gr.model.usuario.Conquista import Conquista


class ConquistaDao(BaseDao):

    def get_by_usuario(self, usuario_id):
        return self.model.query.filter(self.model.usuarioId == usuario_id).order_by(self.model.data.desc(), self.model.descricao.desc()).all()


conquista_dao = ConquistaDao(Conquista)
