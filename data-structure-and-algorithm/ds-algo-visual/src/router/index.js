import { createRouter, createWebHistory } from "vue-router";
import Home from "@/components/Home.vue";
import DynamicArray from "@/components/DynamicArray.vue";
import ComingSoon from "@/components/ComingSoon.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/dynamic-array",
      name: "dynamic-array",
      component: DynamicArray,
    },
    {
      path: "/linked-lists",
      name: "linked-lists",
      component: ComingSoon,
    },
    {
      path: "/stacks",
      name: "stacks",
      component: ComingSoon,
    },
    {
      path: "/queues",
      name: "queues",
      component: ComingSoon,
    },
    {
      path: "/trees",
      name: "trees",
      component: ComingSoon,
    },
    {
      path: "/graphs",
      name: "graphs",
      component: ComingSoon,
    },
    {
      path: "/sorting-algorithms",
      name: "sorting-algorithms",
      component: ComingSoon,
    },
    {
      path: "/searching-algorithms",
      name: "searching-algorithms",
      component: ComingSoon,
    },
  ],
});

export default router;
