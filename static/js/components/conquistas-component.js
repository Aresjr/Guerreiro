const ConquistasComponent = {
    pagina: 'Conquistas',
    titulo: 'Conquistas | Guerreiro',
    rota: '/conquistas',
    rota_view: '/view/conquistas',
    template: '<div id="conquistas-content" style="background-color:#ECF0F1"></div>',
    mounted(){
        $('#nome-pagina').html(ConquistasComponent.pagina);
        document.title = ConquistasComponent.titulo;
        $('#menu-conquistas').addClass('active');

        $ajaxView(ConquistasComponent.rota_view, function(view){
            $('#conquistas-content').html(view);
        });
    },
};

export default ConquistasComponent;