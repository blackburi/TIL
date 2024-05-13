<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" v-model.trim="title">
      <label for="content">내용 : </label>
      <textarea v-model.trim="content"></textarea>
      <input type="submit">
    </form>
  </div>
</template>


<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const router = useRouter()

const title = ref(null)
const content = ref(null)

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
  })
    .then(() => {
      router.push({ name: 'ArticleView' })
    })
    .catch((error) => {
      console.log(error)
    })
}

</script>


<style>
</style>
