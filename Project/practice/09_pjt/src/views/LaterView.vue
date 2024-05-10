<template>
  <div class="container mt-5">
    <h1>저장한 동영상</h1>
    <div class="row" v-if="store.laterVideosList.length">
      <div v-for="video of store.laterVideosList" class="col-lg-4 col-md-6 col-sm-12 mb-4">
        <div class="card" style="width: 18rem;">
          <p class="card-text text-center">{{ video.title }}</p>
          <img :src="video.snippet.thumbnails.high.url" class="card-img-top" alt="#" style="width: 100%; height: 200px;">
          <div class="card-body">
            <button @click="store.later(video.id.videoId)" class="btn">
              <span v-if="store.laterVideos.includes(video.id.videoId)">❤️</span>
              <span v-else>🤍</span>
            </button>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <p>등록된 비디오 없음</p>
    </div>
  </div>
</template>


<script setup>
import { useVideosStore } from '@/stores/videos'
import { useRoute, useRouter, onBeforeRouteUpdate } from 'vue-router'

const route = useRoute()
const videoId = route.params.videoId

const store = useVideosStore()
</script>


<style scoped>
</style>