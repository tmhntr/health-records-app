import { createApp } from "vue";
import App from "./App.vue";
import { router } from "./router";

// 5. Create and mount the root instance.
const app = createApp(App).use(router);

app.mount("#app");
