import { createRouter, createWebHistory } from "vue-router";
import DynamicArray from "@/components/DynamicArray.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: DynamicArray,
    },
  ],
});

export default router;
