// where urls are defined and mapped to components
import { createRouter, createWebHistory } from "vue-router";
import Ping from "../components/Ping.vue";
import Products from "@/components/Products.vue";
import OrderSuccess from "@/components/OrderSuccess.vue";
import OrderCanceled from "@/components/OrderCanceled.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "products",
      component: Products,
    },
    {
      path: "/ping",
      name: "ping",
      component: Ping,
    },
    {
      path: "/success",
      name: "order-success",
      component: OrderSuccess,
    },
    {
      path: "/canceled",
      name: "order-canceled",
      component: OrderCanceled,
    },
  ],
  mode: "hash",
});

export default router;
