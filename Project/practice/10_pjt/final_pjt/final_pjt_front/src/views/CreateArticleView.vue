<template>
  <h1>게시물 작성</h1>
  <hr>
  <div class="main bg-light p-4">
    <div class="row">
      <div class="col-12">
        <div class="card card-body shadow-sm mb-4" style="width: 100%;">
          <form>
            <div>
              <label for="title">제목</label>
              <br>
              <input type="text" id="title" v-model.trim="title">
            </div>
            <hr>
            <div>
              <label for="content">내용</label>
              <br>
              <textarea id="content" v-model.trim="content" style="width: 100%; height: 500px;">
              </textarea>
            </div>
            <hr>
            <button type="button" class="btn btn-outline-secondary"  @click.prevent="createArticle">게시글 등록</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { useBankStore } from '@/stores/bank'
import { ref } from 'vue'

const store = useBankStore()
const title = ref('')
const content = ref('')

const createArticle = function () {
  const payload = {
    title: title.value,
    content: content.value
  }
  store.createArticle(payload)
}
</script>


<style scoped>
</style>
