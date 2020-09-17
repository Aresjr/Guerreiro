$(document).ready(function() {

    $.ajax({
        url: '/api/atividades'
    }).done(function(quadros){

        new SlimSelect({
          select: '#usuario-execucao',
          searchPlaceholder: 'Procurar'
        });

        const addAtividadeClick = function(btn, estagioId){
            $('#modal-atividade-nova').modal('show');
            $('#atividade-estagio').val(estagioId);
        };

        const dragendBoard = function(board){
            $.post({
                url: '/api/trocar_ordem_estagio',
                data: {
                    'estagio_id': board.dataset.id,
                    'ordem': board.dataset.order
                },
                dataType: 'json'
            }).fail(function(error) {
                console.log(error); //TODO - tratar
            });
        };

        const dropEl = function (el, target) {
            el.dataset.estagio = $(target).parent().data('id');

            $.post({
                url: '/api/trocar_estagio_atividade',
                data: {
                    'atividade_id': el.dataset.eid,
                    'estagio_id': el.dataset.estagio
                },
                dataType: 'json'
            }).fail(function(error) {
                console.log(error); //TODO - tratar
            });
        };

        new jKanban({
            element : '#kanban',
            buttonClick: addAtividadeClick,
            dropEl: dropEl,
            dragendBoard: dragendBoard,
            boards: quadros,
            addItemButton: true,
            borderWidth: 320,
            breakLine: false,
            dragBoards: false
        });

    });

    $('#salvar_atividade_nova').click(function(){
        $('#modal-atividade-nova').modal('hide');
        const atividade_nova = $getFormData($('#form-atividade-nova'));

        const card = $createCard({
            title: atividade_nova.codigo,
            descricao: atividade_nova.descricao,
            executor: 'ares'
        });

        $('#atividades-quadro-'+atividade_nova.estagioId).append(card);

        $.post({
            url: `/api/atividade_nova`,
            data: atividade_nova
        }).fail(function(error) {
            console.log(error); //TODO - tratar
        });

    });

});