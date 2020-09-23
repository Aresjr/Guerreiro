import PerfilComponent from '/static/js/components/perfil-component.js';
import KanbanComponent from '/static/js/components/kanban-component.js';
import ConquistasComponent from '/static/js/components/conquistas-component.js';
import CarreiraComponent from '/static/js/components/carreira-component.js';

const components = [
    PerfilComponent,
    KanbanComponent,
    ConquistasComponent,
    CarreiraComponent
]

const rotas = []
components.forEach(function(component){
    component.watch = {
        $route: function(to, from){
            $('#nome-pagina').html(to.meta.pagina);
            document.title = to.meta.titulo;
        }
    };
    rotas.push({
        component: component,
        path: component.rota,
        meta: {
            titulo: component.titulo,
            pagina: component.pagina,
        }
    });
});

export default rotas;