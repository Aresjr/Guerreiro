from datetime import datetime

from app import app, db
from flask import jsonify, request
from flask_login import current_user

from gr.dao.AtividadeDao import atividade_dao
from gr.model.manyToMany.AtividadeEstagio import AtividadeEstagio
from gr.service.EstagioService import estagio_service


@app.route('/api/atividades', methods=["GET"])
def api_atividades_get():
    usuario = current_user
    estagios_json = estagio_service.get_quadro_by_usuario(usuario)
    return jsonify(estagios_json)

@app.route('/api/atividade_estagio', methods=["POST"])
def api_atividade_estagio():
    usuario = current_user
    atividadeid = request.form['atividade_id']
    estagioid = request.form['estagio_id']

    atividade = atividade_dao.get_by_id(atividadeid)
    atividade_estagio = db.session.query(AtividadeEstagio).filter_by(atividade_id=atividadeid, estagio_id=atividade.estagioId, fim_atividade=None).first()

    if atividade_estagio:
        atividade_estagio_update = AtividadeEstagio.update().where(AtividadeEstagio.c.atividade_id == atividadeid)\
            .where(AtividadeEstagio.c.estagio_id == atividade.estagioId)\
            .where(AtividadeEstagio.c.fim_atividade == None).values(fim_atividade=datetime.now())
        db.session.execute(atividade_estagio_update)

    atividade.estagioId = estagioid
    db.session.add(atividade)

    atividade_estagio = AtividadeEstagio.insert().values(atividade_id=atividadeid, estagio_id=estagioid, usuario_id=usuario.id, incio_atividade=datetime.now())
    db.session.execute(atividade_estagio)

    db.session.commit()

    return jsonify({'response': 'OK'})
