<template>
  <router-view></router-view>
</template>

<script lang="ts">
import { defineComponent } from "vue";
// import HelloWorld from "./components/HelloWorld.vue";
// import Home from "./pages/Home.vue";

export default defineComponent({
  name: "App",
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

body {
  box-sizing: border-box;
  margin: 0;
  padding: 0;

  font-family: "Roboto", sans-serif;
  font-size: 16px;
  line-height: 1.5;
  color: #333;

  background-color: #f5f5f5;
}
</style>
