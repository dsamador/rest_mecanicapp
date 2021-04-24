import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import TipoLavado from '../components/TipoLavado'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  { path: '/tipolavado', name: 'tipolavado', component: TipoLavado },  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
