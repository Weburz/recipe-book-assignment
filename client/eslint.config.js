// @ts-check
import withNuxt from "./.nuxt/eslint.config.mjs";

export default withNuxt({
  ignores: ["**/.nuxt/**/*", "**/node_modules/**/*"],
  rules: {
    "vue/html-self-closing": [
      "warn",
      {
        html: {
          void: "always",
        },
      },
    ],
  },
});
