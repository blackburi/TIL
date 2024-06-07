<template>
  <main>
  <section class="vh-lg-100 mt-5 mt-lg-0 bg-soft d-flex align-items-center">
    <div class="container">
      <p class="text-center">
        <RouterLink :to="{name:'home'}" class="text-gray-700"><font-awesome-icon :icon="['fas', 'home']"/>   홈</RouterLink>
      </p>
      <div class="row justify-content-center form-bg-image" data-background-lg="@/assets/img/illustrations/signin.svg">
        <div class="col-12 d-flex align-items-center justify-content-center">
          <div class="bg-white shadow border-0 rounded border-light p-4 p-lg-5 w-100 fmxw-500">
            <div class="text-center text-md-center mb-4 mt-md-0">
              <h1 class="mb-0 h3">로그인</h1>
            </div>
            <form @submit.prevent="login" class="mt-4">
              <div class="form-group mb-4">
                <label for="username">이름</label>
                <div class="input-group">
                  <span class="input-group-text" id="basic-addon1"><font-awesome-icon :icon="['fas', 'signature']" /></span>
                  <input type="text" class="form-control" placeholder="name" id="username" v-model.trim="username" autofocus required>
                </div>  
              </div>
              <div class="form-group">
                <div class="form-group mb-4">
                  <label for="password">비밀번호</label>
                  <div class="input-group">
                    <span class="input-group-text" id="basic-addon2"><font-awesome-icon :icon="['fas', 'key']"/></span>
                    <input type="password" placeholder="Password" class="form-control" id="password" v-model.trim="password" required>
                  </div>  
                </div>
              </div>
              <div class="d-grid">
                <button type="submit" class="btn btn-dark">Sign in</button>
              </div>
            </form>
              <div class="d-flex justify-content-center align-items-center mt-4">
                <span class="fw-normal">
                  계정이 없으신가요?
                  <RouterLink :to="{name:'signup'}" class="fw-bold">회원가입</RouterLink>
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>


<script setup>
import { ref } from 'vue'
import { useBankStore } from '@/stores/bank' 
import { RouterLink } from 'vue-router';

const username = ref(null)
const password = ref(null)

const store = useBankStore()

const login = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.login(payload)
}
</script>


<style scoped>
</style>