<template>
    <div>
      <v-list>
        <v-list-item v-for="recipe in recipes" :key="recipe.id">
          <v-list-item-content>
            <v-list-item-title>
              <nuxt-link :to="`/recipes/${recipe.id}`">{{ recipe.name }}</nuxt-link>
            </v-list-item-title>
          </v-list-item-content>
          <v-list-item-action>
            <v-btn @click="editRecipe(recipe)">Edit</v-btn>
            <v-btn @click="deleteRecipe(recipe.id)" color="red">Delete</v-btn>
          </v-list-item-action>
        </v-list-item>
      </v-list>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        recipes: [],
      };
    },
    async created() {
      const response = await axios.get('/recipes');
      this.recipes = response.data;
    },
    methods: {
      async deleteRecipe(id) {
        await axios.delete(`/recipes/${id}`);
        this.recipes = this.recipes.filter(recipe => recipe.id !== id);
      },
      editRecipe(recipe) {
        this.$router.push({ path: `/add`, query: { id: recipe.id } });
      },
    },
  };
  </script>
  