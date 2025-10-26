<template>
  <div class="movie-page">
    <header class="hero" :style="heroStyle">
      <div class="hero-overlay">
        <img class="poster" :src="posterSrc" alt="poster" v-if="hasPoster" @load="onPosterLoad" :class="{ loaded: posterLoaded }"/>
        <div class="meta">
          <h1>{{ movie.Title || 'Loading...' }}</h1>
          <p class="sub">{{ movie.Genre }} • {{ movie.Released }}</p>
          <p class="plot">{{ movie.Plot }}</p>
          <div class="actions">
            <button>Like</button>
            <button>Watchlist</button>
          </div>
        </div>
      </div>
    </header>

    <main class="content">
      <div class="left">
        <h2>About</h2>
        <p><strong>Director:</strong> {{ movie.Director }}</p>
        <p><strong>Actors:</strong> {{ movie.Actors }}</p>
      </div>

      <aside class="right">
        <h3>Community</h3>
        <PostsFeed api-url="/api/posts/" />
      </aside>
    </main>
  </div>
</template>

<script>
import PostsFeed from './PostsFeed.vue'
export default {
  components: { PostsFeed },
  data() {
    return { movie: {}, posterLoaded: false }
  },
  computed: {
    hasPoster() {
      return this.movie.Poster && this.movie.Poster !== 'N/A'
    },
    posterSrc() {
      return this.movie.Poster
    },
    heroStyle() {
      if (this.hasPoster && this.posterLoaded) {
        return { backgroundImage: `linear-gradient(to right, rgba(3,37,65,0.6), rgba(3,37,65,0.2)), url(${this.movie.Poster})` }
      }
      return { backgroundColor: '#033' }
    }
  },
  methods: {
    fetchMovie() {
      fetch('http://www.omdbapi.com/?i=tt3896198&apikey=d2132124')
        .then(r => r.json())
        .then(data => { this.movie = data })
        .catch(err => console.error(err))
    },
    onPosterLoad() { this.posterLoaded = true }
  },
  mounted() { this.fetchMovie() }
}
</script>

<style scoped>
.movie-page { }
.hero { min-height: 360px; background-size: cover; background-position: center; color: white; }
.hero-overlay { background: rgba(0,0,0,0.45); display:flex; gap:16px; padding:24px; align-items:center; }
.poster { width:160px; border-radius:6px; box-shadow:0 6px 18px rgba(0,0,0,0.5); opacity:0; transition: opacity .3s ease-in; }
.poster.loaded { opacity: 1; }
.meta { max-width: 60%; }
.meta h1 { margin: 0 0 8px; font-size: 1.8rem; }
.plot { margin-top: 12px; color: #ddd; }
.actions button { margin-right: 8px; padding:8px 12px; border-radius:6px; }
.content { display:flex; gap:24px; padding:24px; }
.left { flex: 1; }
.right { width: 360px; }
@media (max-width: 900px) {
  .hero-overlay { flex-direction: column; align-items:flex-start; }
  .meta { max-width: 100%; }
  .poster { width:120px; }
  .content { flex-direction: column; }
  .right { width: 100%; }
}
</style>
