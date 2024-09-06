<template>
  <div class="container">
    <h1>Recipe Book</h1>
    <ul>
      <li v-for="recipe in recipes" :key="recipe.id">
        <nuxt-link :to="'/recipes/' + recipe.id">{{ recipe.title }}</nuxt-link>
      </li>
    </ul>
    <nuxt-link to="/create" class="button">Add New Recipe</nuxt-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      recipes: []
    }
  },
  async mounted() {
    const response = await fetch('http://localhost:8000/recipes')
    this.recipes = await response.json()
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

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 10px 0;
}

a {
  text-decoration: none;
  color: #3498db;
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
