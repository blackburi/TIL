<template>
  <div class="container">
    <div v-if="store.isLogin">
      <p>어서오세요 {{ store.currentUserData.nickname }}님!</p>
    </div>
    <div v-else>
      <p>로그인 또는 회원가입이 필요합니다.</p>
    </div>
  </div>
  <hr>
  <div id="carouselExampleDark" class="carousel carousel-dark slide" data-bs-ride="carousel">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" aria-label="Slide 2"></button>
      <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2" aria-label="Slide 3"></button>
    </div>
    <div class="carousel-inner">
      <div class="carousel-item active" data-bs-interval="10000" @click.prevent="goToMap">
        <img src="../assets/img/illustrations/map.png" class="d-block mx-auto" alt="map">
        <div class="carousel-caption d-none d-md-block custom-caption">
          <h5>근처 은행 찾아보기</h5>
          <p>지역과 은행을 선택하고 지점을 알아보세요!</p>
        </div>
      </div>
      <div class="carousel-item" data-bs-interval="2000" @click.prevent="goToJoin">
        <img src="../assets/img/illustrations/AI.png" class="d-block mx-auto" alt="AI">
        <div class="carousel-caption d-none d-md-block custom-caption">
          <h5>AI</h5>
          <p>자신에게 알맞는 서비스를 추천받아보세요!</p>
        </div>
      </div>
      <div class="carousel-item" @click.prevent="goToProduct">
        <img src="../assets/img/illustrations/product.png" class="d-block mx-auto" alt="product">
        <div class="carousel-caption d-none d-md-block custom-caption">
          <br>
          <h5>금융 상품 찾아보기</h5>
          <p>모든 금융상품을 한눈에 보세요!</p>
        </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>


<script setup>
import { onMounted } from 'vue'
import { useBankStore } from '@/stores/bank'
import { useRouter } from 'vue-router'

const store = useBankStore()
const router = useRouter()

const goToProduct = function () {
  router.push({ name: 'products' })
}

const goToJoin = function () {
  router.push({ name: 'joinproducts' })
}

const goToMap = function () {
  router.push({ name: 'map' })
}

onMounted(() => {
  if (store.isLogin) {
    store.getUserInfo()
    store.getCurrentUser()
  }
})
</script>


<style scoped>
.carousel-item {
  cursor: pointer;
}

.carousel-item img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.custom-caption {
  background-color: rgba(0, 0, 0, 0.5);
  padding: 10px;
  border-radius: 10px;
  bottom: 20px; /* Adjust this to move the caption up or down */
}

.carousel-caption h5,
.carousel-caption p {
  color: #fff;
}

img {
  width: 500px;
  height: 450px;

}
</style>
