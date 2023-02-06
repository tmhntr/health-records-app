<script setup lang="ts">
import { defineProps } from "vue";
// import { useRouter } from "vue-router";

defineProps<{
  card: {
    title: string;
    content: string;
    button_text: string;
    route: string;
  };
}>();

// const on_click = () => {
//   router.push(props.route);
// };
</script>
<template>
  <div class="card">
    <h1 v-if="card.title">{{ card.title }}</h1>
    <p>{{ card.content }}</p>
    <router-link :to="card.route">
      <button>{{ card.button_text }}</button>
    </router-link>
  </div>
</template>

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
