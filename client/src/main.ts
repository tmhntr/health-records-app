import { createApp } from "vue";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faUserSecret } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faFileMedical } from "@fortawesome/free-solid-svg-icons";

import App from "./App.vue";
import { router } from "./router";

library.add(faUserSecret);
library.add(faFileMedical);

// 5. Create and mount the root instance.
const app = createApp(App);
app.use(router);
app.component("font-awesome-icon", FontAwesomeIcon);
app.mount("#app");
