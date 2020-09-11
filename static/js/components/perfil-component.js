const PerfilComponent = {
    pagina: 'Início',
    titulo: 'Guerreiro',
    template: '<div id="perfil" style="padding: 0rem 1.5rem;"></div>',
    mounted(){
        $('#nome-pagina').html(PerfilComponent.pagina);
        document.title = PerfilComponent.titulo;
        $.ajax({
            url: '/view/perfil'
        }).done(function(view) {
            $('#perfil').html(view);
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