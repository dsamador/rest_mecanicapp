import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import TipoLavado from './components/TipoLavado.vue'
import TipoMantenimiento from './components/TipoMantenimiento.vue'
import TipoCombustible from './components/TipoCombustible.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    { path: '/tipolavado', name: 'tipolavado', component: TipoLavado },
    { path: '/tipomantenimiento', name: 'tipomantenimiento', component: TipoMantenimiento },
    { path: '/tipocombustible', name: 'tipocombustible', component: TipoCombustible },
    { path: '/about', name: 'about', component: () => import('./views/About.vue')}
  ]
})
