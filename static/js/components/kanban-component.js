const KanbanComponent = {
    pagina: 'Kanban',
    titulo: 'Kanban | Guerreiro',
    template: '<div id="kanban-content" class="mt-4"></div>',
    mounted(){
        $('#nome-pagina').html(KanbanComponent.pagina);
        $('#menu-kanban').addClass('active');
        document.title = KanbanComponent.titulo;
        $.ajax({
            url: '/view/kanban'
        }).done(function(view) {
            $('#kanban-content').html(view);
            import('/static/js/pages/kanban-on-load.js');
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