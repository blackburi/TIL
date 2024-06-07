<template>
  <h1>상품 세부 정보</h1>
  <hr>
  <div class="box d-flex justify-content-center flex-wrap flex-md-nowrap align-items-center py-4 bg-light">
    <div class="row">
      <div class="col-12">
        <div class="card border-light shadow-sm ">
          <div class="card-body">
            <h3>금융 상품명</h3>
            <p>
              {{ product.fin_prdt_nm }}
              <button @click.prevent="store.interest(product.id)" class="btn">
                <span v-if="store.currentUserData.financial_products.includes(product.id)">❤️</span>
                <span v-else>🤍</span>
              </button>
            </p><hr>
            <h5>금융 회사</h5>
            <p>{{ product.kor_co_nm }}</p>
            <h5>유의 사항</h5>
            <p>{{ product.etc_note }}</p>
            <h5>가입 제한</h5>
            <p>{{ product.join_deny }}</p>
            <h5>가입 대상</h5>
            <p>{{ product.join_member }}</p>
            <h5>가입 방법</h5>
            <p>{{ product.join_way }}</p>
            <h5>우대 조건</h5>
            <p>{{ product.spcl_cnd }}</p>
            <h5>만기후 이자율</h5>
            <p>{{ product.mtrt_int }}</p>
            <hr>
            <div>
              <h3>금융 상품 옵션</h3>
              <br>
              <div v-for="productOption of productOptions">
                <p>타입 : {{ productOption.id - type + 1 }}</p>
                <p>저축 금리 유형 : {{ productOption.intr_rate_type_nm }}</p>
                <p>저축 기간 [단위: 개월] : {{ productOption.save_trm }}</p>
                <p>저축 금리 [소수점 2자리] : {{ productOption.intr_rate }}</p>
                <p>최고 우대 금리 [소수점 2자리] : {{ productOption.intr_rate2 }}</p>
                <button v-if="store.currentUserData.join_products.includes(productOption.id)" type="button" class="btn btn-outline-danger" @click.prevent="store.joinProduct(productOption.id)">가입 취소하기</button>
                <button v-else type="button" class="btn btn-outline-success" @click.prevent="store.joinProduct(productOption.id)">가입하기</button>
                <hr>
              </div>
              <div>
                <button type="button" class="btn btn-outline-primary" @click.prevent="goToProducts">
                  목록으로 돌아가기
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { useRoute } from 'vue-router'
import { useBankStore } from '@/stores/bank'
import { onMounted, ref } from 'vue'
import axios from 'axios';
import router from '@/router';

const route = useRoute()
const store = useBankStore()

const productId = parseInt(route.params.id)
const product = store.products.find((element) => element.id === productId)
const productOptions = ref({})
const type = ref(0)

const fetchProductOptions = (product) => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/deposit-products-options/${product.fin_prdt_cd}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(response => {
      productOptions.value = response.data
      type.value = productOptions.value[0].id
    })
    .catch(error => {
      console.error('Error fetching product options:', error)
    })
}

const goToProducts = function () {
  router.push({name: 'products'})
}

onMounted(() => {
  fetchProductOptions(product)
})
</script>


<style scoped>
.box {
  padding: 20px;
}
</style>