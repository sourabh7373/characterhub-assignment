<template>
  <div id="app">
    <MoviePage />
  </div>
</template>

<script>
import MoviePage from './components/MoviePage.vue'
export default { components: { MoviePage } }
</script>

<style>
body { margin: 0; font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; }
#app { min-height: 100vh; background: #f7f7f8; }
</style>
