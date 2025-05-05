import { createRouter, createWebHistory } from 'vue-router';
import ItemsX from "@/components/ItemsX.vue";
import PtP_schedule from "@/components/PtP_schedule.vue";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: ItemsX
  },
  {
    path: '/p2p_schedule',
    name: 'p2p_schedule',
    component: PtP_schedule
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;