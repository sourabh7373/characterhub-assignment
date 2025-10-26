<template>
  <section class="posts-feed">
    <div v-for="post in posts" :key="post.id" class="post">
      <h3>{{ post.title }}</h3>
      <p>{{ post.body }}</p>
      <small>{{ formatted(post.created_at) }}</small>

      <!-- Like & Watchlist buttons -->
      <div class="buttons">
        <button @click="post.liked = !post.liked">{{ post.liked ? "Liked" : "Like" }}</button>
        <button @click="post.inWatchlist = !post.inWatchlist">{{ post.inWatchlist ? "Added" : "Watchlist" }}</button>
      </div>
    </div>

    <div ref="loadMore" class="observer-target" v-if="hasNext">Loading more...</div>
    <div v-if="loading && !posts.length">Loading...</div>
  </section>
</template>

<script>
export default {
  props: { apiUrl: { type: String, required: true } },
  data() {
    return {
      posts: [],
      nextCursor: null,
      loading: false,
      hasNext: true,
      observer: null
    }
  },
  methods: {
    fetchPage(cursor = null) {
      if (this.loading) return
      this.loading = true
      let url = this.apiUrl
      if (cursor) url += `?cursor=${encodeURIComponent(cursor)}`

      fetch(url)
        .then(r => r.json())
        .then(data => {
          // Add reactive fields liked & inWatchlist BEFORE pushing
          const newPosts = data.results.map(post => ({
            ...post,
            liked: false,
            inWatchlist: false
          }))
          this.posts.push(...newPosts)

          this.hasNext = !!data.next
          if (data.next) {
            try {
              const u = new URL(data.next)
              this.nextCursor = u.searchParams.get('cursor')
            } catch (e) { this.nextCursor = null }
          } else this.nextCursor = null
        })
        .catch(err => console.error(err))
        .finally(() => { this.loading = false })
    },
    formatted(dt) {
      try { return new Date(dt).toLocaleString() } catch(e) { return dt }
    },
    setupObserver() {
      const target = this.$refs.loadMore
      if (!target) return
      this.observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting && this.hasNext && !this.loading) this.fetchPage(this.nextCursor)
      })
      this.observer.observe(target)
    }
  },
  mounted() {
    this.fetchPage()
    this.$nextTick(this.setupObserver)
  },
  beforeUnmount() {
    if (this.observer) this.observer.disconnect()
  }
}
</script>

<style scoped>
.posts-feed { display: flex; flex-direction: column; gap: 12px; }
.post { background: #fff; padding: 12px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.observer-target { text-align: center; padding: 8px; color: #888; }
.buttons { margin-top: 8px; display: flex; gap: 8px; }
button { padding: 6px 12px; border: 1px solid #ccc; border-radius: 4px; cursor: pointer; }
button:hover { background-color: #f0f0f0; }
</style>
