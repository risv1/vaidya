// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  modules: [
    "@nuxtjs/tailwindcss",
    "@vueuse/nuxt",
    "@nuxtjs/color-mode",
    "@nuxt/icon"
  ],
  tailwindcss: {
    config: {
      darkMode: 'class',
    }
  },
  colorMode: {
    classSuffix: '',
    preference: 'light', 
    fallback: 'light',  
  },
  ssr: false,
  imports: {
    dirs: ['./composables']
  }
})
