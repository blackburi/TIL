<template>
  <div class="container mt-5">
    <h1>동영상 목록 페이지</h1>
    <div class="row">
      <div v-for="video of store.videos.items" :key="video.id.videoId" class="col-lg-4 col-md-6 col-sm-12 mb-4">
        <VideoDetail :video="video" />
      </div>
    </div>
  </div>
  <RouterView />
</template>


<script setup>
import VideoDetail from '@/components/VideoDetail.vue'
import { RouterLink, RouterView } from 'vue-router'
import { useVideosStore } from '@/stores/videos'
const store = useVideosStore()

</script>


<style scoped>
</style>