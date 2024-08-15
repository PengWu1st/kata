/// app entry point, which loads and initializes Vue along with root component

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/css/bootstrap.css";

const app = createApp(App);

app.use(router);

app.mount("#app");
