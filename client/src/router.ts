import { createRouter, createWebHistory } from "vue-router";
import Home from "./views/HomePage.vue";
import About from "./views/AboutPage.vue";
import EditRecord from "./views/EditRecordPage.vue";
import ViewRecordsVue from "./views/ViewRecordsPage.vue";
import NotFoundVue from "./views/NotFoundPAge.vue";

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: Home },
    { path: "/about", component: About },
    { path: "/add", component: EditRecord },
    { path: "/edit/:id", component: EditRecord },
    { path: "/view", component: ViewRecordsVue },
    { path: "/:notFound(.*)", component: NotFoundVue },
  ],
});
