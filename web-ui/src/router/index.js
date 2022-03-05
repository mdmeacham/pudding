import Vue from 'vue';
import VueRouter from 'vue-router';
import POC from '../components/POC.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/pocs',
    name: 'pocs',
  },
  {
    path: '/pocs/:poc_id',
    name: 'poc',
    component: POC,
  },
  { path: '/', redirect: { name: 'pocs' } },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
