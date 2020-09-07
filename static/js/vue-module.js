import Vue from 'https://cdn.jsdelivr.net/npm/vue@2.6.11/dist/vue.esm.browser.min.js';
Vue.use(VueRouter);

import PaginaInicialComponent from '/static/js/components/pagina-inicial-component.js';
import KanbanComponent from '/static/js/components/kanban-component.js';

const router = new VueRouter({
  routes: [{
    path: '/',
    component: PaginaInicialComponent
  }, {
    path: '/kanban',
    component: KanbanComponent
  }]
});

new Vue({
    el: '#main-content',
    router
});


