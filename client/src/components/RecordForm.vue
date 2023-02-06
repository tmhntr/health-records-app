<script setup lang="ts">
import { defineProps, ref } from "vue";

const props = defineProps<{
  title?: string;
  description?: string;
  record_id?: string;
}>();

const title = ref(props.title);
const description = ref(props.description);
// const record_id = props.record_id;

const user_id = 1;

const post_record = async () => {
  const response = await fetch(
    `https://health.timhunter.dev/api/v1/users/${user_id}/records`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title: title.value,
        description: description.value,
      }),
    }
  );
  const data = await response.json();
  console.log(data);
};
</script>
<!-- A form to post a health record to the api endpoint /Users/{user_id}/Records -->
<template>
  <!-- a form with title and description inputs -->
  <div class="record-form">
    <h1>Add Record</h1>
    <form>
      <label for="title">Title</label>
      <input type="text" id="title" name="title" v-model="title" />
      <label for="content">Content</label>
      <textarea
        id="description"
        name="description"
        v-model="description"
      ></textarea>
      <button type="submit" @click.prevent="post_record">Submit</button>
    </form>
  </div>
</template>

<style scoped>
.record-form {
  background-color: #ffffff;
  border: 0.5em solid #42b983;
  border-radius: 2em;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin: 20px auto;
  width: 300px;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  width: 350px;
  height: 350px;
}

.record-form > * {
  margin: 0.5rem;
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
  width: 350px;
  height: 350px;
}

.button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  border: 1px solid #ccc;
  border-radius: 3px;
  cursor: pointer;
}

.button:hover {
  background-color: #ccc;
}
</style>
