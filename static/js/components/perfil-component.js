const PerfilComponent = {
    pagina: 'Início',
    titulo: 'Guerreiro',
    rota: '/',
    rota_view: '/view/perfil',
    template: '<div id="perfil" class="ml-4 mr-4"></div>',
    mounted(){
        $('#nome-pagina').html(PerfilComponent.pagina);
        document.title = PerfilComponent.titulo;
        $('#menu-pagina-inicial').addClass('active');

        $ajaxView(PerfilComponent.rota_view, function(view){
            $('#perfil').html(view);
            import('/static/js/pages/perfil-page.js');
        });
    }
};

export default PerfilComponent;