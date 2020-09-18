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
            var allowedBoards = [];
            jkanban.options.boards.map(function (board) {
                if (board.id === el.dataset.estagio) {
                    board.dragTo.map(function (_board) {
                        if (allowedBoards.indexOf(_board) === -1) {
                            allowedBoards.push(_board);
                        }
                    });
                    return allowedBoards[0];
                }
                return allowedBoards[0];
            });
            const estagio_novo = $(target).parent().data('id').toString();
            if (allowedBoards.length > 0 && allowedBoards.indexOf(estagio_novo) === -1) {
                return;
            }

            el.dataset.estagio = estagio_novo;

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

        var jkanban = new jKanban({
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

    $('#form-atividade-nova').on('submit', function(e){
        e.preventDefault();
        $('#modal-atividade-nova').modal('hide');
        const atividade_nova = $getFormData(this);

        const card = $createCard({
            title: atividade_nova.codigo,
            descricao: atividade_nova.descricao,
            executor: $( "#usuario-execucao option:selected").data('username')
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