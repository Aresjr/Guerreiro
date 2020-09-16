const KanbanComponent = {
    pagina: 'Kanban',
    titulo: 'Kanban | Guerreiro',
    template: '<div id="kanban-content" class="mt-4"></div>',
    mounted(){
        $('#nome-pagina').html(KanbanComponent.pagina);
        // $('#menu-kanban').addClass('active');
        document.title = KanbanComponent.titulo;
        const request = $.ajax({
            url: '/view/kanban'
        });
        request.success(function(response) {
            console.log(response);
            $('#kanban-content').html(response);
            import('/static/js/pages/kanban-on-load.js');
        });
        request.error(function(httpObj, textStatus){
            console.log('error');
            console.log(httpObj);
            console.log(textStatus);
        });
    },
    watch:{
        $route: function(to, from){
            $('#nome-pagina').html(to.meta.pagina);
            document.title = to.meta.titulo;
        }
    }
};

export default KanbanComponent;