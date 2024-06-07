<template>
  <h1>커뮤니티</h1>
  <hr>
  <div class="d-flex justify-content-center flex-wrap flex-md-nowrap align-items-center py-4 bg-light">
    <div class="row">
      <div class="col-12">
        <button type="button" class="btn btn-outline-dark" style="margin-left: 55px; margin-bottom: 20px;" @click="goToCreate">
          게시물 생성
        </button>
        <div class="card border-light shadow-sm" style="margin-left: 50px;">
          <div class="card-body">
            <div class="mt-3 mb-3" style="margin-left:50px; margin-right:50px">
              <table v-if="articles.length" class="table table-hover text-center">
                <thead class="bg-primary text-white">
                  <tr>
                    <th class="border-gray-200">게시글 번호</th>
                    <th class="border-gray-200" style="width:700px;">제목</th>
                    <th class="border-gray-200">관심 게시글</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="article of articles" :key="article.id" @click="goToDetail(article.id)">
                    <td>{{ article.id }}</td>
                    <td>제목 : {{ article.title }} | 좋아요 수 : {{ article.like_users.length }}</td>
                    <td>
                      <button @click.stop.prevent="store.interestArticle(article, currentUser.id)" class="btn">
                        <span v-if="article.like_users.includes(currentUser.id)">❤️</span>
                        <span v-else>🤍</span>
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
              <table v-else>
                아직 등록된 게시물이 없습니다.
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useBankStore } from '@/stores/bank'
import { onMounted, ref, watchEffect } from 'vue'

const store = useBankStore()
store.getProducts()
const currentUser = store.currentUserData
const articles = ref([])
const router = useRouter()

const fetchArticles = () => {
  store.getArticles()
  articles.value = store.articles
}

const goToDetail = function (id) {
  router.push({ name: 'articledetail', params: { articleId: id } })
}

const goToCreate = function () {
  router.push({ name: 'createarticle' })
}

onMounted(() => {
  fetchArticles()
})

watchEffect(() => {
  articles.value = store.articles
})
</script>


<style scoped>
button {
  cursor: pointer;
}

table {
  cursor: pointer;
}
</style>