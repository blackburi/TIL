import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ProductsView from '@/views/ProductsView.vue'
import DetailView from '@/views/DetailView.vue'
import ProfileView from '@/views/ProfileView.vue'
import exchangeRateView from '@/views/exchangeRateView.vue'
import MapView from '@/views/MapView.vue'
import CommunityView from '@/views/CommunityView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import CreateArticleView from '@/views/CreateArticleView.vue'
import JoinProductsView from '@/views/JoinProductsView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView
    },
    {
      path: '/products',
      name: 'products',
      component: ProductsView
    },
    {
      path: '/products/:id',
      name: 'detail',
      component: DetailView
    },
    {
      path: '/profile/:userId',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/exchangerate',
      name: 'exchangerate',
      component: exchangeRateView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/articledetail/:articleId',
      name: 'articledetail',
      component: ArticleDetailView
    },
    {
      path: '/createarticle',
      name: 'createarticle',
      component: CreateArticleView
    },
    {
      path:'/joinproducts',
      name:'joinproducts',
      component:JoinProductsView,
    },
  ]
})

export default router