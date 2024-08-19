<template>
  <div>
    <h1>Recipe Book</h1>
    <RecipeList />
    <nuxt-link to="/add">
      <v-btn color="primary">Add new Recipe</v-btn>
    </nuxt-link>
  </div>
</template>

<script>
import RecipeList from '@/components/RecipeList.vue';

export default {
  components: {
    RecipeList,
  },
};
</script>
