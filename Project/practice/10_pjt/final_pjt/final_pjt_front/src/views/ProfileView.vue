<template>
  <h1>개인 정보 상세/수정/탈퇴 페이지</h1>
  <hr>
  <h4>{{ store.currentUserData.username }}님의 정보입니다.</h4>
  <div class="main bg-light p-4">
    <div class="row">
      <div class="col-12">
        <div class="card card-body shadow-sm mb-4 ">
          <form>
            <div class="row">
              <div class="col-md-12 mb-3">
                <div class="form-group">
                  <label for="userName">이름</label>
                  <input
                    v-model="updatedUserData.username"
                    class="form-control"
                    id="userName"
                    type="text"
                    :placeholder=store.currentUserData.username
                    readonly
                  />
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-12 mb-3">
                <div class="form-group">
                  <label for="nickname">별명</label>
                  <input
                    v-model="updatedUserData.nickname"
                    class="form-control"
                    id="nickname"
                    type="text"
                    :placeholder=store.currentUserData.nickname
                  />
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-12 mb-3">
                <div class="form-group">
                  <label for="email">이메일</label>
                  <input
                    v-model="updatedUserData.email"
                    class="form-control"
                    id="email"
                    type="email"
                    :placeholder=store.currentUserData.email
                  />
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-12 mb-3">
                <div class="form-group">
                  <label for="password">Password</label>
                  <input
                    v-model="updatedUserData.password"
                    class="form-control"
                    id="password"
                    type="password"
                    placeholder="********"
                  />
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-12 mb-3">
                <div class="form-group">
                  <label for="age">나이</label>
                  <input
                    v-model="updatedUserData.age"
                    class="form-control"
                    id="age"
                    type="number"
                    :placeholder=store.currentUserData.age
                  />
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-12 mb-3">
                <div class="form-group">
                  <label for="number">현재 소유 금액 (만원)</label>
                  <input
                    v-model="updatedUserData.money"
                    class="form-control"
                    id="number"
                    type="number"
                    :placeholder=store.currentUserData.money
                  />
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-12 mb-3">
                <div class="form-group">
                  <label for="salary">연봉 (만원):</label>
                  <input
                    v-model="updatedUserData.salary"
                    class="form-control"
                    id="salary"
                    type="number"
                    :placeholder=store.currentUserData.salary
                  />
                </div>
              </div>
            </div>
            <hr>
            <div class="row mb-3 mt-3">
              <div class="col">
                <div class="form-group">
                  <div class="btn-group" style="float:right;">
                    <button
                    type="submit"
                    id="successAlert"
                    @click.prevent="updateUserInfo"
                    class="btn btn-outline-dark"
                    >
                      <font-awesome-icon :icon="['fas', 'user-edit']" /> 수정
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </form>
        </div>
        <div class="card-body">
          <div class="row">
            <div class="form-group">
              <div class="btn-group " style="float:right;">
                <button type="submit" @click="confirmDeleteAccount" class="btn btn-outline-danger">
                  <font-awesome-icon :icon="['fas', 'eraser']" /> 탈퇴
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- <div class="col-12 col-xl-4">
        <div class="row">
          <div class="col-12 mb-4">
            <div class="card shadow-sm text-center p-0">
              <div
                class="profile-cover rounded-top"
                style="background: linear-gradient(to bottom, #262b40, #FFFFFF)"
              ></div>
              <div class="card-body pb-5">
                <img
                  :src="this.$store.state.userInfo.userProfileImageUrl"
                  class="user-avatar large-avatar rounded-circle mx-auto mt-n7 mb-4"
                  alt="Neil Portrait"
                />
                <h4 class="h3">{{ this.$store.state.userInfo.userName }}</h4>

                <p class="text-gray mb-4">{{ this.$store.state.userInfo.userMessage }}</p>
              </div>
            </div>
          </div>
            <div class="col-12">
            <div class="card card-body shadow-sm mb-4">
              <h2 class="h5 mb-4">Select profile photo</h2>
              <div class="d-flex align-items-center mb-4">
                <div class="me-3">
                  <div class="user-avatar xl-avatar">
                    <img class="rounded" v-if="imageUrl" :src="imageUrl" alt="change avatar" />
                  </div>
                </div>
                <div class="file-field">
                  <div class="d-flex justify-content-xl-center ms-xl-3">
                    <div class="d-flex">
                      <span class="icon icon-md"
                        ><font-awesome-icon :icon="['fas', 'paperclip']" class="me-3"
                      /></span>
                      <input
                        ref="imageInput"
                        type="file"
                        hidden
                        @change="onChangeImages"
                        id="inputFileUploadInsert"
                      />
                      <div class="d-md-block text-left">
                          <div class="fw-normal text-dark mb-1">Choose Image</div>
                        <div class="text-gray small">JPG, GIF or PNG. Max size of 800K</div>
                      </div>
                    </div>
                  </div>
                  <div class="btn-group mb-2" style="float:right;">
                    <button
                      type="submit"
                      @click="onClickImageUpload"
                      class="btn btn-outline-dark btn-sm"
                    >
                      <font-awesome-icon :icon="['fas', 'image']" /> 사진 선택
                    </button>
                    <button
                      type="submit"
                      @click="onClickImageSend"
                      class="btn btn-sm btn-outline-secondary"
                    >
                      <font-awesome-icon :icon="['fas', 'upload']" /> 사진 업로드
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div> 
        </div>
      </div> -->
    </div>
  </div>
  <!-- <secession-modal v-on:call-parent-secession-close="closeAfterSecession"></secession-modal> -->
</template>


<script setup>
import { onMounted, ref } from 'vue'
import { useBankStore } from '@/stores/bank'
import { useRoute, useRouter, RouterLink, RouterView } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const store = useBankStore()
const productsNumbers = ref([])

const userId = ref(route.params.userId)

onMounted(() => {
  store.getUserInfo()
  store.getCurrentUser()
  productsNumbers.value = store.currentUserData.financial_products
})

const deleteAccount = () => {
  axios({
    method: 'delete',
    url: `http://127.0.0.1:8000/users/delete-user/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then(() => {
    alert('회원 탈퇴가 완료되었습니다.')
    store.logout()
    router.push({ name: 'home' })
  })
  .catch((error) => {
    console.error('회원 탈퇴 중 오류 발생:', error)
    alert('회원 탈퇴 중 오류가 발생했습니다. 다시 시도해 주세요.')
  })
}

const confirmDeleteAccount = () => {
  if (confirm('정말로 회원탈퇴를 하시겠습니까?')) {
    deleteAccount()
  }
}


const updatedUserData = ref({
  nickname: store.currentUserData.nickname,
  email: store.currentUserData.email,
  age: store.currentUserData.age,
  money: store.currentUserData.money,
  salary: store.currentUserData.salary
})

const updateUserInfo = () => {
  axios({
    method: 'put',
    url: `http://127.0.0.1:8000/users/current-user/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: updatedUserData.value
  })
    .then((response) => {
      store.currentUserData = response.data
      alert('회원 정보가 성공적으로 업데이트되었습니다.')
      router.push({ name: 'profile', params:{ userId: store.currentUserData.id} })
    })
    .catch((error) => {
      alert('회원 정보를 바르게 수정해 주세요.')
    })
}


</script>


<style scoped>
</style>