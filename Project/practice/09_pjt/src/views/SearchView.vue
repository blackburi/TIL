<template>
  <div class="mx-4 my-4">
    <div class="d-flex" role="search">
      <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model="inputText">
      <button class="btn btn-outline-danger" type="submit" @click="onInput">Search</button>
    </div>
  </div>
  <HomeView />
</template>


<script setup>
import { ref } from 'vue'
import HomeView from './HomeView.vue'
import { useVideosStore} from '@/stores/videos'

const store = useVideosStore()
const inputText = ref('')

const onInput = function () {
  store.fetchVideo(inputText.value)
}

</script>


<style scoped>
</style>