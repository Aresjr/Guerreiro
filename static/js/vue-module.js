import Vue from 'https://cdn.jsdelivr.net/npm/vue@2.6.11/dist/vue.esm.browser.min.js';

import PerfilComponent from '/static/js/components/perfil-component.js';
import KanbanComponent from '/static/js/components/kanban-component.js';
import ConquistasComponent from '/static/js/components/conquistas-component.js';

$(document).ready(function() {

    Vue.use(VueRouter);

    const router = new VueRouter({
        routes: [{
            path: PerfilComponent.rota,
            component: PerfilComponent,
            meta: {
                titulo: PerfilComponent.titulo,
                pagina: PerfilComponent.pagina,
            }
        }, {
            path: KanbanComponent.rota,
            component: KanbanComponent,
            meta: {
                titulo: KanbanComponent.titulo,
                pagina: KanbanComponent.pagina
            }
        }, {
            path: ConquistasComponent.rota,
            component: ConquistasComponent,
            meta: {
                titulo: ConquistasComponent.titulo,
                pagina: ConquistasComponent.pagina
            }
        }]
    });

    new Vue({
        el: '#main-content',
        router
    });

});