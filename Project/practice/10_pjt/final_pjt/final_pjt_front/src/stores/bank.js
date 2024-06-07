import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useBankStore = defineStore('bank', () => {
  const products = ref([])
  const articles = ref([])
  const token = ref(null)
  const id = ref(null)
  const currentUserData = ref({})
  const userdata = ref([])
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'

  const getProducts = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/products/`,
    })
    .then((response) => {
      products.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/list/`,
    })
    .then((response) => {
      // console.log(response.data)
      articles.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }

  const createArticle = function (payload) {
    const { title, content } = payload
    axios({
      method: 'post',
      url: `${API_URL}/articles/list/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        title, content,
      }
    })
    .then((response) => {
      router.push({ name: 'community' })
    })
    .catch((error) => {
      console.log(error)
    })
  }

  // DB에 저장된 모든 사용자를 불러오는 함수
  const getUserInfo = function () {
    axios({
      method: 'get',
      url: `${API_URL}/users/save-users/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((response) => {
      // 요청이 성공했을 때 실행되는 코드
      // console.log('사용자 정보:', response.data);
      userdata.value = response.data
    })
    .catch((error) => {
      console.error('사용자 정보를 불러오는 중 오류 발생:', error);
    })
  }

  const getCurrentUser = function () {
    if (isLogin.value) {
      axios({
        method: 'get',
        url: `${API_URL}/users/current-user/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      .then((response) => {
        // 현재 사용자 정보
        currentUserData.value = response.data
        // if (userdata.value.financial_products) {
        //   interestProdcuts.value = userdata.value.financial_products.split(',').map(id => parseInt(id, 10))
        // }
      })
      .catch((error) => {
        console.error('현재 사용자 정보를 불러오는 중 오류 발생:', error)
      })
    }
  }

  const signup = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password = payload.password1
    const nickname = payload.nickname
    const email = payload.email
    const age = payload.age
    const money = payload.money
    const salary = payload.salary
    axios({
      method: 'post',
      url: `${API_URL}/users/save-users/`,
      data: {
        username, password, nickname, email, age, money, salary,
      }
    })
      .then((response) => {
        console.log('회원가입 성공')
        const password = password1
        login({ username, password })
      })
      .catch((error) => {
        console.log(error)
        alert('정보를 올바르게 입력해주세요')
      })
  }

  const login = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        token.value = response.data.key
        getCurrentUser()
        router.push({ name: 'home' })
      })
      .catch((error) => {
        alert('이름과 비밀번호가 일치하지 않거나 존재하지 않습니다. 바르게 입력하거나 회원가입을 진행해 주세요.')
        console.log(error)
      })
  }

  const logout = function () {
    token.value = null
    userdata.value = {}
    router.push({ name: 'login' })
  }

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const interest = function (productId) {
    if (currentUserData.value.financial_products.includes(productId)) {
      const Index = currentUserData.value.financial_products.findIndex((id) => id === productId)
      currentUserData.value.financial_products.splice(Index, 1)
    } else {
      currentUserData.value.financial_products.push(productId)
    }
    updateUserFinancialProducts()
  }

  const updateUserFinancialProducts = function () {
    axios({
      method: 'put',
      url: `${API_URL}/users/update-financial-products/`,
      headers: {
        Authorization: `Token ${token.value}`
      }, 
      data: {
        financial_products: currentUserData.value.financial_products
      }
    })
    .then((response) => {
      console.log('사용자 금융 상품 정보 업데이트 성공')
    })
    .catch((error) => {
      console.error('사용자 금융 상품 정보 업데이트 중 오류 발생:', error)
    })
  }

  const interestArticle = function (article, userId) {
    if (article.like_users.includes(userId)) {
      const Index = article.like_users.findIndex((id) => id === userId)
      article.like_users.splice(Index, 1)
    } else {
      article.like_users.push(userId)
    }
    updateArticleLikeUsers(article)
  }

  const updateArticleLikeUsers = function (article) {
    axios({
      method: 'put',
      url: `${API_URL}/articles/update_like_users/${article.id}/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        articleId: article.id
      }
    })
    .then((response) =>{
      console.log('좋아요 업데이트 성공')
    })
    .catch((error) => {
      console.log('좋아요 업데이트 중 오류 발생: ' , error)
    })
  }

  const joinProduct = function (optionId) {
    const index = currentUserData.value.join_products.findIndex((element) => element === optionId);
    if (index !== -1) {
      currentUserData.value.join_products.splice(index, 1)
      alert('해당 상품 옵션에 가입이 취소되었습니다.')
    } else {
      currentUserData.value.join_products.push(optionId)
      alert('해당 상품 옵션에 가입이 완료되었습니다.')
    }
    updateUserJoinProducts()
  }
  
  const updateUserJoinProducts = function () {
    const joinProductIds = currentUserData.value.join_products
    axios({
      method: 'put',
      url: `${API_URL}/users/update_join_products/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        join_products: joinProductIds
      }
    })
    .then((response) => {
      console.log('가입 상품 업데이트 성공')
    })
    .catch((error) => {
      console.log('가입 상품 업데이트 중 오류 발생: ', error)
    })
  }

  return { products, articles, token, id, userdata, currentUserData, isLogin,
    getProducts, getArticles, createArticle,
    getUserInfo, getCurrentUser, signup, login, logout,
    interest, updateUserFinancialProducts, interestArticle, updateArticleLikeUsers,
    joinProduct, updateUserJoinProducts,
  }
}, { persist : true})