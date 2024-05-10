<template>
  <div class="container mt-5">
    <h1>상세 정보</h1>
    <hr>
    <h3>{{ video.snippet.title }}</h3>
    <iframe id="player" type="text/html" width="640" height="360"
    :src="'http://www.youtube.com/embed/' + videoId + '?enablejsapi=1&origin=http://example.com'"
  frameborder="0">
    </iframe>
    <hr>
    <p>Description : {{ video.snippet.description }}</p>
    <button @click="store.later(videoId)" class="btn">
      <span v-if="store.laterVideos.includes(videoId)">❤️</span>
      <span v-else>🤍</span>
    </button>
  </div>
</template>


<script setup>
import { useVideosStore } from '@/stores/videos'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const videoId = route.params.videoId

const store = useVideosStore()
const video = store.videos.items.find((element) => element.id.videoId === videoId)
</script> 


<style scoped> 
</style>