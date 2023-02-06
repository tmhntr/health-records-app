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
  <div class="cards-container">
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

<style>
.cards-container {
  margin: 0 auto;

  display: grid;
  grid-template: repeat(3, 1fr) / 1fr;
  grid-gap: 1rem;
  padding: 1rem;

  width: 100%;

  justify-content: center;
  align-items: center;
}

/* make it responsive */
@media (min-width: 768px) {
  .cards-container {
    grid-template: 1fr / repeat(3, 1fr);
  }
}

.card {
  border: 1px solid #ccc;
  border-radius: 3px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  margin: 1rem;
  width: 100%;
  height: 100%;
}
</style>
