$(document).ready(function() {

    $.ajax({
        url: '/api/atividades'
    }).done(function(quadros){

        new SlimSelect({
          select: '#usuario-execucao'
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
                console.log(error);
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
                console.log(error);
            });
        };

        new jKanban({
            element : '#kanban',
            buttonClick: addAtividadeClick,
            dropEl: dropEl,
            dragendBoard: dragendBoard,
            boards: quadros,
            addItemButton: true,
            borderWidth: 338,
            breakLine: false,
            dragBoards: false
        });

    });

    $('#salvar_atividade_nova').click(function(){
        $('#modal-atividade-nova').modal('hide');
        const atividade_nova = $getFormData($('#form-atividade-nova'));
        console.log(jKanban.createCard);
        console.log(createCard);
        //TODO - Adicionar visualmente o card ao estágio (coluna)

        $.post({
            url: `/api/atividade_nova`,
            data: atividade_nova
        }).done(function(response) {
            console.log(response);
        }).fail(function(error) {
            console.log(error);
        });

    });

});