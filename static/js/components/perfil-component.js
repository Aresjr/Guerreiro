const PerfilComponent = {
    pagina: 'Início',
    titulo: 'Guerreiro',
    rota: '/',
    rota_view: '/view/perfil',
    template: '<div id="perfil" class="ml-4 mr-4"></div>',
    watch: {
        $route: function(to, from){
            $('#nome-pagina').html(to.meta.pagina);
            document.title = to.meta.titulo;
        }
    },
    mounted(){
        $('#nome-pagina').html(PerfilComponent.pagina);
        document.title = PerfilComponent.titulo;
        $('#menu-pagina-inicial').addClass('active');

        $ajaxView(PerfilComponent.rota_view, function(view){
            $('#perfil').html(view);
        });
    }
};

export default PerfilComponent;