const ConquistasComponent = {
    pagina: 'Conquistas',
    titulo: 'Conquistas | Guerreiro',
    rota: '/conquistas',
    rota_view: '/view/conquistas',
    template: '<div id="conquistas-content" style="background-color:#f8f9fc"></div>',
    watch: {
        $route: function(to, from){
            $('#nome-pagina').html(to.meta.pagina);
            document.title = to.meta.titulo;
        }
    },
    mounted(){
        $('#nome-pagina').html(ConquistasComponent.pagina);
        document.title = ConquistasComponent.titulo;
        $('#menu-conquistas').addClass('active');

        console.log(this.rota);
        $ajaxView(ConquistasComponent.rota_view, function(view){
            $('#conquistas-content').html(view);
        });
    },
};

export default ConquistasComponent;