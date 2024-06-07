<template>
  <button type="button" class="btn btn-outline-dark" @click.prevent="goToCommunity"> 게시물 목록 돌아가기</button>

  <br>
  <br>
  <h1>게시물 상세 페이지</h1>
  <div class="main bg-light p-4">
    <div class="row">
      <div class="col-12">
        <div v-if="article.user == currentUser.id && !editFlag" style="margin-bottom: 20px;">
          <button type="button" class="btn btn-outline-success" style="margin-right: 10px;" @click.prevent="editArticle">게시물 수정</button>
          <button type="button" class="btn btn-outline-danger" @click.prevent="deleteArticle(article.id)">게시물 삭제</button>
        </div>
        <div class="card card-body shadow-sm mb-4 ">
          <div class="row">
            <div class="col-md-12 mb-3">
                <b>작성자 : {{ writer.username }} </b>
                <p> {{ article.created_at.slice(0,10) }}  {{ article.created_at.slice(11,19) }}</p>
                <hr>
                <br>
                <div v-if="editFlag" class="title">
                  <h4>제목 수정</h4>
                  <input type="text" v-model="updatedTitle"/>
                  <hr>
                  <h4>내용 수정</h4>
                  <textarea v-model="updatedContent" style="width: 500px; height: 500px;"></textarea>
                  <br>
                  <button type="button" class="btn btn-outline-success" @click.prevent="updateArticle(article.id)" style="margin-right: 10px;">저장</button>
                  <button type="button" class="btn btn-outline-danger"  @click.prevent="cancelEdit">취소</button>
                </div>
                <div v-else>
                  <!-- <h4>제목</h4> -->
                  <h3>{{ updatedTitle }}</h3>
                  <br>
                  <p>{{ updatedContent }}</p>
                </div>
              </div>
              
              <div class="large d-flex justify-content-start mb-4" style="width: 100%;">
                <ul class="list-group list-group-horizontal">
                  <li class="list-group-item">
                    <button @click.prevent="store.interestArticle(article, currentUser.id)" class="btn">
                      <span v-if="article.like_users.includes(currentUser.id)"><font-awesome-icon :icon="['fas', 'thumbs-up']" /></span>
                      <span v-else><font-awesome-icon :icon="['far', 'thumbs-up']" /></span>
                    </button>
                    <span>{{ article.like_users.length }}</span>
                  </li>
                  <li class="list-group-item">
                    <div style="margin-top: 7px; margin-left: 10px;">
                      <span style="margin-right: 15px;"><font-awesome-icon :icon="['fas', 'comment']" /></span>
                      <span>{{ comments.length }}</span>
                    </div>
                  </li>
                </ul>
              </div>
              <div class="shadow-line"></div>
              <div>
                <h4>댓글</h4>
                <ul v-if="comments.length">
                  <li v-for="comment of comments">
                    <p>{{ comment.content }}</p>
                    <p v-if="comment.user == currentUser.id">
                      <div v-if="check != comment.id">
                        <button type="button" class="btn btn-outline-success" @click.prevent="change(comment.id)" style="display: inline-block; margin-right: 10px;">수정</button>
                        <button type="button" class="btn btn-outline-danger" @click.prevent="deleteComment(comment.id)" style="display: inline-block;">삭제</button>
                      </div>
                      <div v-if="check == comment.id">
                        <div>
                          <br>
                          <div>
                            <textarea type="text" id="content" v-model.trim="content" style="width: 500px;height: 150px;"></textarea>
                          </div>
                          <br>
                          <button type="button" class="btn btn-outline-secondary" @click.prevent="updateComment(comment.id)">수정 완료</button>
                        </div>
                      </div>
                    </p>
                  </li>
                </ul>
                <ul v-else>
                  <p>아직 등록된 댓글이 없습니다.</p>
                </ul>
              </div>
              <hr>
              <div>
              <div class="card-footer py-3 border-0" style="background-color: #f8f9fa;">
                <form>
                  <div class="d-flex flex-start w-100">
                  <div data-mdb-input-init class="form-outline w-100">
                    <textarea class="form-control" type="text" id="content" v-model.trim="content" rows="4"
                    style="background: #fff;"></textarea>
                  </div>
                </div>
                <div class="float-end mt-3 pt-1">
                  <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-outline-success btn-sm" @click.prevent="createComment">댓글 작성</button>
                  <!-- <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-outline-primary btn-sm">Cancel</button> -->
                </div>
              </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <hr>
</template>


<script setup>
import { useBankStore } from '@/stores/bank'
import axios from 'axios'
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const store = useBankStore()
const articleId = parseInt(route.params.articleId)

const article = ref({})
const writer = ref({})

article.value = store.articles.find((element) => element.id === articleId)
writer.value = store.userdata.find((element) => element.id === article.value.user)
const currentUser = store.currentUserData
const editFlag = ref(false)
const updatedTitle = ref('')
updatedTitle.value = article.value.title
const updatedContent = ref('')
updatedContent.value = article.value.content

const comments = ref([])
const content = ref(null)
const check = ref(0)


onMounted(async () => {
  store.getArticles()
  getComments()
})

const deleteArticle = function (articleId) {
  const article = store.articles.find((element) => element.id === articleId)
  axios({
    method:'delete',
    url: `http://127.0.0.1:8000/articles/delete_article/${article.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      articleId: article.id
    }
  })
  .then((response) => {
    router.push({ name: 'community' })
  })
  .catch((error) => {
    console.log(error)
  })
}

const updateArticle = function (articleId){
  const article_local = store.articles.find((element) => element.id === articleId)
  axios({
    method:'put',
    url: `http://127.0.0.1:8000/articles/article_update/${article_local.id}/`,
    headers:{
      Authorization: `Token ${store.token}`
    },
    data:{
      title:updatedTitle.value,
      content:updatedContent.value,
    }
  })
  .then((response)=>{
    console.log(response)
    editFlag.value = false
    store.getArticles()
  })
  .catch((err)=>{
    console.log(err)
  })
}

const editArticle = function () {
  editFlag.value = true
  updatedTitle.value = article.value.title
  updatedContent.value = article.value.content
}

const cancelEdit = function () {
  editFlag.value = false
  updatedTitle.value = article.value.title
  updatedContent.value = article.value.content
}

const getComments = function () {
  axios({
    method:'get',
    url: `http://127.0.0.1:8000/articles/${article.value.id}/comment/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      articleId: article.value.id,
      
    }
  })
  .then((response) => {
    comments.value = response.data
    content.value = ''
  })
  .catch((error) => {
    console.log(error)
  })
}

const deleteComment = function (commentId) {
  const comment = comments.value.find((element) => element.id === commentId)
  axios({
    method: 'delete',
    url: `http://127.0.0.1:8000/articles/${articleId}/update_comment/${comment.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      articleId: article.id,
      commentId: comment.id,
    }
  })
  .then((response) => {
    getComments()
  })
  .catch((error) => {
    console.log(error)
  })
}

const createComment = function () {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/articles/${article.value.id}/comment/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      content: content.value,
      articleId: article.value.id
    }
  })
  .then((response) => {
    getComments()
  })
  .catch((error) => {
    console.log(error)
  })
}

const change = function (commentId) {
  check.value = commentId-check.value
}

const updateComment = function (commentId) {
  const comment = comments.value.find((element) => element.id === commentId)
  axios({
    method: 'put',
    url: `http://127.0.0.1:8000/articles/${articleId}/update_comment/${comment.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      content: content.value,
      articleId: article.id,
      commentId: comment.id,
    }
  })
  .then((response) => {
    getComments()
    change()
    content.value = ''
    check.value = commentId-check.value
  })
  .catch((error) => {
    console.log(error)
  })
}

const goToCommunity = function() {
  router.push({name:'community'})
}

</script>


<style scoped>
.row {
  display: flex;
  gap: 10px; /* form 태그 사이에 간격을 두고 싶으면 사용 */
  align-items: center; /* 수직 정렬을 중앙으로 맞추기 위해 사용 */
}

.shadow-line {
  height: 1px;
  background: #000;
  box-shadow: 0 1px 5px rgba(0, 0, 0, 0.3);
  margin: 20px 0;
}

.title{
  height: 700px;
  align-items: center;
  justify-content: center;
}
</style>