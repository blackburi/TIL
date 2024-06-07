<template>
  <h1>가입한 상품 목록</h1>
  <hr>

  <div class="row ">
    <div class="col-12">
      <div class="card border-light shadow-sm ">
        <div class="card-body">
          <div class="mt-3 mb-3" style="margin-left:50px; margin-right:50px">
            <div v-if="products.length">
              <table class="table table-hover text-center">
                <thead class="bg-primary text-white">
                  <tr>
                    <th class="border-gray-200">은행명</th>
                    <th class="border-gray-200" style="width:700px;">상품명</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="productname in productnames" :key="productname.id" @click="goToDetail(productname.id)">
                    <td>{{ productname.kor_co_nm }}</td>
                    <td>{{ productname.fin_prdt_nm }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div v-else>
              <br>
              가입한 상품이 없습니다.
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <br>
  <br>
  <h1>가입한 상품 금리를 한번에 모아서 보세요</h1>
  <hr>
  <div v-if="chartData">
    <div class="row justify-content-center">
      <Bar :data="chartData" :options="chartOptions" />
    </div>

  </div>

  <hr>
  <h1>가입한 상품 기반으로 AI가 추천한 상품이에요</h1>
  <p>tensorflow의 model을 사용해 다른 사용자들이 가입한 상품을 기반으로 추천해요</p>
  <br>

    <div class="row">
    <div class="col-sm-3 mb-3 mb-sm-0" v-for="product of recommendProducts">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">{{ product.fin_prdt_nm }}</h5>
          <p class="card-text">{{ product.kor_co_nm }}</p>
          <a @click="goToDetail(product.id)" class="btn btn-primary">상품 정보 보기</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>

import { onMounted, ref, watch } from 'vue'
import { useBankStore } from '@/stores/bank'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const route = useRoute()
const router = useRouter()
const store = useBankStore()
const productOptions = ref([])
const products = store.products
const productnames = ref([])
const recommendProductsCd = ref({})
const recommendProducts = ref([])

const userId = store.currentUserData.id

const getProductsByOptions = () => {
  const productIds = productOptions.value.map(option => option.product)
  return store.products.filter(product => productIds.includes(product.id))
}

const fetchProductOptions = () => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/user_join_options/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(response => {
      productOptions.value = response.data
    })
    .catch(error => {
      console.error('Error fetching product options:', error)
    })
}

const goToDetail = function (id){
  router.push({ name: 'detail', params:{ id: id } })
}

const chartData = ref(null)
const chartOptions = ref({
  responsive: true,
  plugins: {
    legend: {
      position: 'top',
      labels: {
        font: {
          family: 'Gowun Batang',
          size: 14, 
        },
        color: 'black'
      },
    },
    title: {
      display: true,
      text: '가입한 상품 금리',
      labels: {
        font: {
          family: 'Gowun Batang',
          size: 40, 
        },
      },
    },
    tooltip: {
      opacity: 1.0,
    },
  },
  elements: {
    bar: {
      borderWidth: 2, // Set border width for bars
      borderColor: 'rgba(0,0,0,0.2)', // Set border color for bars
    },
  },
  scales: {
    y: {
      beginAtZero: true,
      ticks: {
        font: {
          family: 'Gowun Batang',
          size: 14,
        },
      },
    },
    x: {
      ticks: {
        font: {
          family: 'Gowun Batang',
          size: 14,
        },
      },
    },
  },
})


const loadChartData = () => {
  const productIds = productOptions.value.map(option => option.product)
  productnames.value = store.products.filter(product => productIds.includes(product.id))
  const labels = ref([])
  for (const productId of productIds) {
    const product = products.value.find((element) => element.id === productId)
    labels.value.push(product.fin_prdt_nm)
  }
  
  // label로 product name을 선택
  const intrRates = productOptions.value.map(option => option.intr_rate)
  const intrRates2 = productOptions.value.map(option => option.intr_rate2)

  const averageRate = intrRates.reduce((sum, rate) => sum + rate, 0) / intrRates.length
  const averageRate2 = intrRates2.reduce((sum, rate) => sum + rate, 0) / intrRates2.length

  const averageRatesArray = Array(intrRates.length).fill(averageRate)
  const averageRates2Array = Array(intrRates2.length).fill(averageRate2)

  chartData.value = {
    labels: labels.value,
    datasets: [
      {
        label: '저축금리',
        backgroundColor: '#7F92DB',
        data: intrRates,
      },
      {
        label: '최고우대금리',
        backgroundColor: '#80AFDC',
        data: intrRates2,
      },
    ],
  }
}

watch(productOptions, (newOptions) => {
  products.value = getProductsByOptions()
  loadChartData()
})



onMounted(() => {
  store.getUserInfo()
  store.getCurrentUser()
  fetchProductOptions()
  axios({
    method:'get',
    url:`http://localhost:8000/api/recommend/${userId}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
  .then((response)=>{
    // response.json()
    return response
  })
  .then((response)=>{
    recommendProductsCd.value = response.data.recommendations
    recommendProducts.value = store.products.filter(product => recommendProductsCd.value.includes(product.fin_prdt_cd))
  })
})
</script>



<style scoped>
@import url("@/assets/styles/main.css");

.chart-container{
  width: 70%;
  height: 40%;
  display: flex;
  justify-content: center;
}

table {
  cursor: pointer;
}
</style>
