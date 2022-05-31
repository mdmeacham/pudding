import { createRouter, createWebHistory } from 'vue-router';
import POCs from '../components/POCs.vue';
import POC from '../components/POC.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/pocs',
    },
    {
      path: '/pocs',
      name: 'pocs',
      component: POCs,
      children: [
        {
          path: '/pocs/:id',
          name: 'poc',
          component: POC,
        },
      ],
    },
  ],
});

export default router;
