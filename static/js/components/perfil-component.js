const PerfilComponent = {
    template: '<div id="perfil" style="padding:1rem;"></div>',
    mounted(){
        $.ajax({
            url: '/view/perfil'
        }).done(function(view) {
            $('#perfil').html(view);
        });
    }
};

export default PerfilComponent;