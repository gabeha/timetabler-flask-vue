import { createRouter, createWebHistory } from "vue-router";
import Index from "../views/Index.vue";
import Schedule from "../views/Schedule.vue"


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: Index,
    },
    {
      path: "/schedule",
      name: "schedule",
      component: Schedule,
    },
  ],
});

export default router;
