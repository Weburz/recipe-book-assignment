<template>
    <div>
      <v-form @submit.prevent="submitForm">
        <v-text-field v-model="form.name" label="Recipe Name" required></v-text-field>
        <v-textarea v-model="form.description" label="Recipe Description" required></v-textarea>
        <v-file-input v-model="form.image" label="Add Image" required></v-file-input>
        <v-btn type="submit" color="primary">Save</v-btn>
      </v-form>
    </div>
  </template>
  
  <script>
  export default {
    props: ['initialData'],
    data() {
      return {
        form: {
          name: '',
          description: '',
          image: null,
        },
      };
    },
    created() {
      if (this.initialData) {
        this.form = { ...this.initialData };
      }
    },
    methods: {
      submitForm() {
        this.$emit('submit', this.form);
      },
    },
  };
  </script>
  