import Vue from 'https://cdn.jsdelivr.net/npm/vue@2.6.11/dist/vue.esm.browser.min.js';
import rotas from '/static/js/rotas.js';

$(document).ready(function() {

    Vue.use(VueRouter);

    new Vue({
        el: '#main-content',
        router: new VueRouter({
            routes: rotas
        })
    });

});