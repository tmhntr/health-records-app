<script setup lang="ts">
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { ref } from "vue";

import Card from "../components/CardView.vue";

const cards = ref([
  {
    title: "Add Record",
    content: "Add in medical records to keep track your personal medical data.",
    button_text: "+",
    route: "/add",
  },
  {
    title: "View My Records",
    content: "View your personal medical records in a list view.",
    button_text: "View",
    route: "/view",
  },
  {
    title: "About",
    content:
      "Check out some more information on this app, and its development!",
    button_text: "Read more",
    route: "/about",
  },
]);
</script>

<template>
  <div class="hero">
    <font-awesome-icon
      icon="fa-solid fa-file-medical"
      class="fa-8x fa-fade"
      style="--fa-animation-duration: 4s; --fa-fade-opacity: 0.8"
    />
    <h1>Health Records App</h1>
    <h2>Developed by Tim Hunter</h2>
  </div>
  <div class="cards__container">
    <Card
      v-for="card in cards"
      :key="card.title"
      :title="card.title"
      :content="card.content"
      :button_text="card.button_text"
      :card="card"
    />
  </div>
</template>
