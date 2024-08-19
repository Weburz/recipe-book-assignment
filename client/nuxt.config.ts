export default {
  srcDir: 'src/',
  buildModules: ['@nuxt/typescript-build'],
  modules: ['@nuxtjs/axios', '@nuxtjs/vuetify'],
  axios: {
    baseURL: 'http://localhost:8000/api',
  },
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
  },
}

