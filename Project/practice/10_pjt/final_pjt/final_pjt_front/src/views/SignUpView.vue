<template>
  <main>
  <!-- Section -->
    <section class="vh-lg-100 mt-5 mt-lg-0 bg-soft d-flex align-items-center">
      <div class="container">
        <p class="text-center">
          <RouterLink :to="{name:'home'}" class="text-gray-700"><font-awesome-icon :icon="['fas', 'home']"/>   홈</RouterLink>
        </p>
        <div class="row justify-content-center form-bg-image" data-background-lg="@/assets/img/illustrations/signin.svg">
          <div class="col-12 d-flex align-items-center justify-content-center">
            <div class="bg-white shadow border-0 rounded border-light p-4 p-lg-5 w-100 fmxw-500">
              <div class="text-center text-md-center mb-4 mt-md-0">
                <h1 class="mb-0 h3">회원가입</h1>
              </div>
              <form @submit.prevent="signUp" class="mt-4">
                <!-- Form -->
                <div class="form-group mb-4">
                  <label for="username">이름</label>
                  <div class="input-group">
                    <span class="input-group-text" id="basic-addon1"><font-awesome-icon :icon="['fas', 'signature']" /></span>
                    <input type="text" class="form-control" placeholder="name" id="username" v-model.trim="username" autofocus required>
                  </div>  
                </div>
                <!-- End of Form -->
                <div class="form-group">
                  <!-- Form -->
                  <div class="form-group mb-4">
                    <label for="password1">비밀번호</label>
                    <div class="input-group">
                      <span class="input-group-text" id="basic-addon2"><font-awesome-icon :icon="['fas', 'key']"/></span>
                      <input type="password" placeholder="Password" class="form-control" id="password1" v-model.trim="password1" required>
                    </div>  
                  </div>
                </div>
                <!-- End of Form -->
                <div class="form-group">
                  <!-- Form -->
                  <div class="form-group mb-4">
                    <label for="password1">비밀번호 확인</label>
                    <div class="input-group">
                      <span class="input-group-text" id="basic-addon2"><font-awesome-icon :icon="['fas', 'key']"/></span>
                      <input type="password" placeholder="Password confirm" class="form-control" id="password2" v-model.trim="password2" required>
                    </div>  
                  </div>
                </div>
                <!-- End of Form -->
                <div class="form-group">
                  <!-- Form -->
                  <div class="form-group mb-4">
                    <label for="nickname">닉네임</label>
                    <div class="input-group">
                      <span class="input-group-text" id="basic-addon2"><font-awesome-icon :icon="['fas', 'key']"/></span>
                      <input type="text" placeholder="nickname" class="form-control" id="nickname" v-model.trim="nickname" required>
                    </div>  
                  </div>
                </div>
                <!-- End of Form -->
                <div class="form-group">
                  <!-- Form -->
                  <div class="form-group mb-4">
                    <label for="email">이메일</label>
                    <div class="input-group">
                      <span class="input-group-text" id="basic-addon2"><font-awesome-icon :icon="['fas', 'key']"/></span>
                      <input type="text" placeholder="example@company.com" class="form-control" id="email" v-model.trim="email" required>
                    </div>  
                  </div>
                </div>
                <!-- End of Form -->
                <div class="form-group">
                  <!-- Form -->
                  <div class="form-group mb-4">
                    <label for="age">나이</label>
                    <div class="input-group">
                      <span class="input-group-text" id="basic-addon2"><font-awesome-icon :icon="['fas', 'key']"/></span>
                      <input type="number" class="form-control" id="age" v-model.trim="age" required>
                    </div>  
                  </div>
                </div>
                <!-- End of Form -->
                <div class="form-group">
                  <!-- Form -->
                  <div class="form-group mb-4">
                    <label for="money">현재 소유 금액(만원) :</label>
                    <div class="input-group">
                      <span class="input-group-text" id="basic-addon2"><font-awesome-icon :icon="['fas', 'key']"/></span>
                      <input type="number" class="form-control" id="money" v-model.trim="money" required>
                    </div>  
                  </div>
                </div>
                <!-- End of Form -->
                <div class="form-group">
                  <!-- Form -->
                  <div class="form-group mb-4">
                    <label for="salary">연봉(만원) :</label>
                    <div class="input-group">
                      <span class="input-group-text" id="basic-addon2"><font-awesome-icon :icon="['fas', 'key']"/></span>
                      <input type="number" class="form-control" id="salary" v-model.trim="salary" required>
                    </div>  
                  </div>
                </div>
                <!-- End of Form -->
                <div class="d-grid">
                  <button type="submit" class="btn btn-dark">Sign Up</button>
                </div>
              </form>
              <div class="d-flex justify-content-center align-items-center mt-4">
                <span class="fw-normal">
                  계정이 이미 있으신가요?
                  <RouterLink :to="{name:'login'}" class="fw-bold">로그인</RouterLink>
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

const store = useBankStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const email = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)

const signUp = function() {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    email: email.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
  }
  store.signup(payload)
}
</script>


<style scoped>
</style>