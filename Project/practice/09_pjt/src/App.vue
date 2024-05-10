<template>
  <nav class="navbar bg-dark">
    <div class="container-fluid text-center">
      <div class="w-100" id="navbarNav">
        <a class="mx-4" href="#">
          <RouterLink to='/'>Home</RouterLink>
        </a>
        <a class="mx-4" href="#">
          <RouterLink to='/search'>Search</RouterLink>
        </a>
        <a class="ml-4" href="#">
          <RouterLink to='/later'>Later</RouterLink>
        </a>
        <p class="circle">
          {{ store.laterVideosList.length }}
        </p>
      </div>
    </div>
  </nav>
  <div>

  </div>
  <RouterView />
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useVideosStore } from '@/stores/videos'
const store = useVideosStore()
</script>


<style scoped>
.navbar {
  color: white; /* 글자 색을 흰색으로 설정 */
}

.circle{
  width: 20px;
  height: 20px;
  border-radius: 100%;
  background-color: red;
  display: inline-block;
  margin: 0px 10px 0px 10px;
}
</style>
