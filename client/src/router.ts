import { createRouter, createWebHistory } from "vue-router";
import Home from "./views/HomePageView.vue";
import About from "./views/About.vue";
import EditRecord from "./views/EditRecord.vue";
import ViewRecordsVue from "./views/ViewRecords.vue";
import NotFoundVue from "./views/NotFound.vue";

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: Home },
    { path: "/about", component: About },
    { path: "/edit/:id", component: EditRecord },
    { path: "/view", component: ViewRecordsVue },
    { path: "/:notFound(.*)", component: NotFoundVue },
  ],
});
