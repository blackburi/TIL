<template>
  <h1>전체 상품 목록</h1>
  <hr>
  <div class=" justify-content-center flex-wrap flex-md-nowrap align-items-center py-4 bg-light">
    <div class="row">
      <div class="box col-12">
        <h6>필터링 정보</h6>
        <div class="row">
          <div class="col align-self-center">
            <select name="bankname" id="bankname" v-model="selectBank" class="form-select select" aria-label="은행 이름">
              <option value="선택 없음" selected disabled>은행 이름</option>
              <option v-for="bankname of banknames" :key="bankname" :value="bankname">{{ bankname }}</option>
            </select>
          </div>
          <div class="col align-self-center">
            <select name="DepoSave" id="DepoSave" v-model="selectDepoSaves" class="form-select select" aria-label="구">
              <option value="선택 없음" selected disabled>예금/적금</option>
              <option v-for="DepoSave of DepoSaves" :key="DepoSave" :value="DepoSave">{{ DepoSave }}</option>
            </select>
          </div>
          <!-- <div class="col align-self-center">
            <select name="month" id="month" v-model="selectMonths" class="form-select select" aria-label="은행">
              <option value="선택 없음" selected disabled>개월 수</option>
              <option v-for="month of months" :key="month" :value="month">{{ month }}</option>
            </select>
          </div> -->
        </div>
        <br>
        <div class="card border-light ">
          <div class="card-body mr-4" style="width: 100%;">
            <div class="mt-3 mb-3" style="margin-left:50px; margin-right:50px">
              <table class="table table-hover text-center">
                <thead class="bg-primary text-white">
                  <tr>
                    <th class="border-gray-200">상품 번호</th>
                    <th class="border-gray-200" style="width:700px;">상품명</th>
                    <th class="border-gray-200">관심 상품</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="product in filteredProducts" :key="product.id" @click="goToDetail(product.id)">
                    <td>{{ product.id }}</td>
                    <td>{{ product.kor_co_nm }} - {{ product.fin_prdt_nm }}</td>
                    <td>
                      <button @click.stop.prevent="store.interest(product.id)" class="btn">
                        <span v-if="store.currentUserData.financial_products.includes(product.id)">❤️</span>
                        <span v-else>🤍</span>
                      </button>
                    </td>
                  </tr>
                </tbody>
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
import { ref, computed } from 'vue'

const store = useBankStore()
const products = store.products
const router = useRouter()

const banknames = ref(['선택 없음', '경남은행', '광주은행', '국민은행', '농협은행주식회사', '대구은행', '부산은행', '수협은행', '신한은행', '우리은행', '전북은행', '재주은행', '주식회사 카카오뱅크', '주식회사 케이뱅크', '중소기업은행', '토스뱅크 주식회사', '하나은행', '한국산업은행', '한국스탠다드차타드은행']) 
const DepoSaves = ref(['선택 없음', '예금', '적금'])
// const months = ref(['선택 없음', 1, 3, 6, 12, 24, 36])

const selectBank = ref('선택 없음')
const selectDepoSaves = ref('선택 없음')
// const selectMonths = ref('선택 없음')

const filteredProducts = computed(() => {
  return products.filter(product => {
    const matchesBank = selectBank.value === '선택 없음' || product.kor_co_nm === selectBank.value
    const matchesDepoSave = selectDepoSaves.value === '선택 없음' || product.DSname === selectDepoSaves.value
    return matchesBank && matchesDepoSave
  })
})

const goToDetail = function (id) {
  router.push({ name: 'detail', params: { id: id } })
}
</script>

<style scoped>
thead {
  color: blue;
}

table {
  cursor: pointer;
}

.card {
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #ddd;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.box {
  padding: 20px 50px;
}

.card-content {
  text-align: center;
}
</style>