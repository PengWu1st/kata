// where urls are defined and mapped to components
import { createRouter, createWebHistory } from "vue-router";
import Ping from "../components/Ping.vue";
import Products from "@/components/Products.vue";
import OrderSuccess from "@/components/OrderSuccess.vue";
import OrderCanceled from "@/components/OrderCanceled.vue";
import InPageCheckout from "@/components/InPageCheckout.vue";
import InPageCheckoutReturn from "@/components/InPageCheckoutReturn.vue";

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
    {
      path: "/checkout",
      name: "checkout",
      component: InPageCheckout,
    },
    {
      path: "/checkout-return",
      name: "checkout-return",
      component: InPageCheckoutReturn,
    },
  ],
  mode: "hash",
});

export default router;
