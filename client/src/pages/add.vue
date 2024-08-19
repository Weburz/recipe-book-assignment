<template>
    <div>
      <h1>Add New Recipe</h1>
      <RecipeForm @submit="saveRecipe" />
    </div>
  </template>
  
  <script>
  import RecipeForm from '@/components/RecipeForm.vue';
  import axios from 'axios';
  
  export default {
    components: {
      RecipeForm,
    },
    methods: {
      async saveRecipe(form) {
        const formData = new FormData();
        formData.append('name', form.name);
        formData.append('description', form.description);
        formData.append('image', form.image);
  
        await axios.post('/recipes', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
  
        this.$router.push('/');
      },
    },
  };
  </script>
  