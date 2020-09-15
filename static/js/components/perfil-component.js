const PerfilComponent = {
    pagina: 'Início',
    titulo: 'Guerreiro',
    template: '<div id="perfil" class="ml-4 mr-4"></div>',
    mounted(){
        $('#nome-pagina').html(PerfilComponent.pagina);
        $('#menu-pagina-inicial').addClass('active');
        document.title = PerfilComponent.titulo;
        $.ajax({
            url: '/view/perfil'
        }).done(function(view) {
            $('#perfil').html(view);
        }).fail(function(e){
            console.log('fail');
            console.log(e);
        });
    },
    watch:{
        $route: function(to, from){
            $('#nome-pagina').html(to.meta.pagina);
            document.title = to.meta.titulo;
        }
    }
};

export default PerfilComponent;