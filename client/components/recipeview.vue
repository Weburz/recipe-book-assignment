<template>
    <div>
      <h2>{{ recipe.name }}</h2>
      <p>{{ recipe.description }}</p>
      <v-img :src="recipe.image_url"></v-img>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        recipe: {},
      };
    },
    async fetch() {
      const { id } = this.$route.params;
      const response = await axios.get(`/recipes/${id}`);
      this.recipe = response.data;
    },
  };
  </script>
  