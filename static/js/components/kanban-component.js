const KanbanComponent = {
    template: '<div id="kanban-content"></div>',
    mounted(){
        $.ajax({
            url: '/view/kanban'
        }).done(function(view) {
            $('#kanban-content').html(view);
            import('/static/js/pages/kanban-on-load.js');
        });
    }
};

export default KanbanComponent;