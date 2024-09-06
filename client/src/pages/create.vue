<template>
  <div class="container">
    <h1>Create New Recipe</h1>
    <form @submit.prevent="createRecipe">
      <div class="form-group">
        <label for="title">Title:</label>
        <input type="text" v-model="title" id="title" required>
      </div>
      <div class="form-group">
        <label for="ingredients">Ingredients:</label>
        <textarea v-model="ingredients" id="ingredients" required></textarea>
      </div>
      <div class="form-group">
        <label for="instructions">Instructions:</label>
        <textarea v-model="instructions" id="instructions" required></textarea>
      </div>
      <button type="submit" class="button">Create</button>
    </form>
    <nuxt-link to="/" class="button">Back to Recipes</nuxt-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      ingredients: '',
      instructions: ''
    }
  },
  methods: {
    async createRecipe() {
      const response = await fetch('http://localhost:8000/recipes', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          title: this.title,
          ingredients: this.ingredients,
          instructions: this.instructions
        })
      })
      if (response.ok) {
        this.$router.push('/')
      }
    }
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

.form-group {
  margin-bottom: 15px;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 5px;
}

input, textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
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
