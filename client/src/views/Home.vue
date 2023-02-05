<template>
  <div class="home">
    <h1>Home</h1>
    <div class="card-container">
      <Card v-for="card in cards" :key="card.title" :card="card" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Card from "../components/Card.vue";

export default {
  components: { Card },
  data() {
    return {
      cards: [
        { title: "Card 1", content: "Content 1", button_text: "Button 1" },
        { title: "Card 2", content: "Content 2", button_text: "Button 2" },
        { title: "Card 3", content: "Content 3", button_text: "Button 3" }
      ]
    }
  }
};
</script>
