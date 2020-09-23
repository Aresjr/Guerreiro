const CarreiraComponent = {
    pagina: 'Carreira',
    titulo: 'Carreira | Guerreiro',
    rota: '/carreira',
    rota_view: '/view/carreira',
    template: '<div id="carreira-content"></div>',
    mounted(){
        $('#nome-pagina').html(CarreiraComponent.pagina);
        document.title = CarreiraComponent.titulo;
        $('#menu-carreira').addClass('active');

        $ajaxView(CarreiraComponent.rota_view, function(view){
            $('#carreira-content').html(view);
        });
    },
};

export default CarreiraComponent;