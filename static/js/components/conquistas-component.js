const ConquistasComponent = {
    pagina: 'Conquistas',
    titulo: 'Conquistas | Guerreiro',
    template: '<div id="conquistas-content" style="background-color:#f8f9fc"></div>',
    mounted(){
        $('#nome-pagina').html(ConquistasComponent.pagina);
        $('#menu-conquistas').addClass('active');
        document.title = ConquistasComponent.titulo;
        $.ajax({
            url: '/view/conquistas'
        }).done(function(view) {
            $('#conquistas-content').html(view);
        });
    },
    watch:{
        $route: function(to, from){
            $('#nome-pagina').html(to.meta.pagina);
            document.title = to.meta.titulo;
        }
    }
};

export default ConquistasComponent;