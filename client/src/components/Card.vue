<template>
  <div class="card">
    <h1 v-if="title">{{ title }}</h1>
    <p>{{ content }}</p>
    <button @click="() => on_click()">{{ button_text }}</button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "CardComponent",
  components: {},
  props: {
    title: {
      type: String,
      required: false,
      default: null,
    },
    content: {
      type: String,
      required: false,
      default: null,
    },
    button_text: {
      type: String,
      required: true,
      default: null,
    },
    on_click: {
      type: Function,
      required: true,
      default: null,
    },
  },
});
</script>

<style scoped>
.card {
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin: 20px;
  width: 300px;
}

.card h1 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 400;
}

.card p {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 300;
}

.card button {
  background-color: #42b983;
  border: none;
  border-radius: 5px;
  color: #fff;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 400;
  margin: 10px 0 0;
  padding: 10px;
  width: 100%;
}

.card button:hover {
  background-color: #3ca575;
}

.card button:active {
  background-color: #3ca575;
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.2);
}
</style>
