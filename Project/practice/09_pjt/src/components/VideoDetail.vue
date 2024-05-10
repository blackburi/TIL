<template>
  <RouterLink :to="{ name : 'detail', params: {'videoId' : video.id.videoId } }">
    <div class="card" style="width: 300px; height:350px ">
      <img :src="video.snippet.thumbnails.high.url" class="card-img-top" alt="#" style="width: 100%; height: 200px;">
      <b class="card-text text-center">{{ video.snippet.title }}</b>
      <div class="card-body">
        <p class="card-text text-center">{{ video.snippet.channelTitle }}</p>
        </div>
      </div>
    </RouterLink>
  <RouterView />
</template>


<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useVideosStore } from '@/stores/videos'
const store = useVideosStore()

defineProps({
  video: Object
})
</script>


<style scoped>
</style>