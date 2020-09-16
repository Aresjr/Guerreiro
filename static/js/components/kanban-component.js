const KanbanComponent = {
    pagina: 'Kanban',
    titulo: 'Kanban | Guerreiro',
    rota: '/kanban',
    rota_view: '/view/kanban',
    template: '<div id="kanban-content" class="mt-4"></div>',
    mounted(){
        $('#nome-pagina').html(KanbanComponent.pagina);
        document.title = KanbanComponent.titulo;
        $('#menu-kanban').addClass('active');

        $ajaxView(KanbanComponent.rota_view, function(view){
            $('#kanban-content').html(view);
            import('/static/js/pages/kanban-on-load.js');
        });
    }
};

export default KanbanComponent;