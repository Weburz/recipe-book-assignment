<template>
  <div class="container">
    <h1>{{ recipe.title }}</h1>
    <p><strong>Ingredients:</strong> {{ recipe.ingredients }}</p>
    <p><strong>Instructions:</strong> {{ recipe.instructions }}</p>
    <nuxt-link to="/" class="button">Back to Recipes</nuxt-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      recipe: {}
    }
  },
  async asyncData({ params }) {
    const response = await fetch(`http://localhost:8000/recipes/${params.id}`)
    const recipe = await response.json()
    return { recipe }
  }
}
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

p {
  text-align: left;
}

.button {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #3498db;
  color: white;
  border-radius: 5px;
  text-decoration: none;
}

.button:hover {
  background-color: #2980b9;
}
</style>
