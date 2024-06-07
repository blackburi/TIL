<template>
  <div class="layout">
    <nav id="sidebarMenu" class="sidebar d-md-block bg-dark text-white " data-simplebar>
      <div class="sidebar-inner px-2 pt-3">
        <ul class="nav flex-column pt-3 pt-md-0">
          <li class="nav-item mt-2 mb-3" >
            <!-- :class="{ active: $store.state.curPage == 'home' }" -->
            <RouterLink :to="{name:'home'}" class="nav-link">
              <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'home']"/></span>
              <span class="sidebar-text"> Home</span>
            </RouterLink>
          </li>
          <li v-if="store.isLogin" class="nav-item mb-2 mt-2">
            <div>
              <span class="nav-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse" data-bs-target="#searchSub2" aria-expanded="false" aria-controls="searchSub2">
                <span>
                  <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'search']"/></span>
                  <span class="sidebar-text"> service</span>
                </span>
                <span class="link-arrow"><font-awesome-icon :icon="['fas', 'chevron-right']"/></span>
              </span>
            </div>
            <div class="multi-level collapse" id="searchSub2">
              <ul class="flex-column nav">
                <li class="nav-item" >
                  <!-- :class="{ active: $store.state.curPage == 'home' }" -->
                  <RouterLink :to="{name:'exchangerate'}" class="nav-link">
                    <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'circle-info']"/></span>
                    <span class="sidebar-text"> 환율 정보</span>
                  </RouterLink>
                </li>
                <li class="nav-item" >
                  <!-- :class="{ active: $store.state.curPage == 'searchApt' }" -->
                  <RouterLink :to="{name:'products'}" class="nav-link">
                    <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'building']"/></span>
                    <span class="sidebar-text"> 전체 상품 목록</span>
                  </RouterLink>
                </li>
                <li class="nav-item" >
                  <!-- :class="{ active: $store.state.curPage == 'searchApt' }" -->
                  <RouterLink :to="{name:'map'}" class="nav-link">
                    <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'map-marker']"/></span>
                    <span class="sidebar-text"> 주변 은행 검색</span>
                  </RouterLink>
                </li>
                <li class="nav-item" >
                  <!-- :class="{ active: $store.state.curPage == 'searchApt' }" -->
                  <RouterLink :to="{name:'community'}" class="nav-link">
                    <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'image']"/></span>
                    <span class="sidebar-text"> 커뮤니티</span>
                  </RouterLink>
                </li>
              </ul>
            </div>
          </li>
          <li v-else></li>
          <li class="nav-item mb-2 mt-2">
            <div>
              <span class="nav-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse" data-bs-target="#searchSub" aria-expanded="false" aria-controls="searchSub">
                <span>
                  <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'search']"/></span>
                  <span class="sidebar-text"> user info</span>
                </span>
                <span class="link-arrow"><font-awesome-icon :icon="['fas', 'chevron-right']"/></span>
              </span>
            </div>
            <div v-if="!store.isLogin" class="multi-level collapse" id="searchSub">
              <ul class="flex-column nav">
                <li class="nav-item" > 
                  <!-- :class="{ active: $store.state.curPage == 'searchDong' }" -->
                  <RouterLink :to="{name:'signup'}" class="nav-link">
                    <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'map-marked-alt']"/></span>
                    <span class="sidebar-text"> 회원가입</span>
                  </RouterLink>
                </li>
                <li class="nav-item" >
                  <!-- :class="{ active: $store.state.curPage == 'searchApt' }" -->
                  <RouterLink :to="{name:'login'}" class="nav-link">
                    <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'key']"/></span>
                    <span class="sidebar-text"> 로그인</span>
                  </RouterLink>
                </li>
              </ul>
            </div>
            <div v-else>
              <div class="multi-level collapse" id="searchSub">
                <ul class="flex-column nav">
                  <li class="nav-item" >
                    <!-- :class="{ active: $store.state.curPage == 'searchApt' }" -->
                    <RouterLink :to="{name:'profile', params:{'userId' : store.currentUserData.id}}" class="nav-link">
                      <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'user']"/></span>
                      <span class="sidebar-text"> 마이 페이지</span>
                    </RouterLink>
                  </li>
                  <li class="nav-item" >
                    <!-- :class="{ active: $store.state.curPage == 'searchApt' }" -->
                    <RouterLink :to="{name:'joinproducts'}" class="nav-link">
                      <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'table']" /></span>
                      <span class="sidebar-text"> 가입한 상품 정보</span>
                    </RouterLink>
                  </li>
                  <li class="nav-item" >
                    <!-- :class="{ active: $store.state.curPage == 'searchApt' }" -->
                    <span class="nav-link">
                      <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'right-to-bracket']"/></span>
                      <span @click.prevent="store.logout" class="sidebar-text"> 로그아웃</span>
                    </span>
                  </li>
                </ul>
              </div>
            </div>
          </li>
          <!-- <li class="nav-item mb-2 mt-2">
            <div>
              <span class="nav-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse" data-bs-target="#bookmarkSub" aria-expanded="false" aria-controls="bookmarkSub">
                <span>
                  <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'star']"/></span>
                  <span class="sidebar-text"> MY관심</span>
                </span>
                <span class="link-arrow"><font-awesome-icon :icon="['fas', 'chevron-right']"/></span>
              </span>
            </div>
            <div class="multi-level collapse" id="bookmarkSub">
              <ul class="flex-column nav">
                <li class="nav-item" :class="{ active: $store.state.curPage == 'bookmarkArea' }">
                  <RouterLink to="/bookmarkArea" class="nav-link">
                    <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'map-marked-alt']"/></span>
                    <span class="sidebar-text"> 관심 지역 모아 보기</span>
                  </RouterLink>
                </li>
                <li class="nav-item" :class="{ active: $store.state.curPage == 'bookmarkHouse' }">
                  <RouterLink to="/bookmarkHouse" class="nav-link">
                    <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'building']"/></span>
                    <span class="sidebar-text"> 관심 매물 모아 보기</span>
                  </RouterLink>
                </li>
              </ul>
            </div>
          </li>
          <li class="nav-item mb-2 mt-2" :class="{ active: $store.state.curPage == 'info' }">
            <RouterLink to="/info" class="nav-link">
              <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'info-circle']"/></span>
              <span class="sidebar-text"> 지역 정보 검색 </span>
            </RouterLink>
          </li>
          <li class="nav-item mt-2 mb-2" :class="{ active: $store.state.curPage == 'schoolZone' }">
            <RouterLink to="/schoolZone" class="nav-link">
              <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'school']"/></span>
              <span class="sidebar-text"> 주변 학군 검색 </span>
            </RouterLink>
          </li>
          <li class="nav-item mt-2 mb-2" :class="{ active: $store.state.curPage == 'community' }">
            <RouterLink to="/community" class="nav-link">
              <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'comment-dots']"/></span>
              <span class="sidebar-text"> 커뮤니티</span>
            </RouterLink>
          </li>
          <li class="nav-item mt-2 mb-2" :class="{ active: $store.state.curPage == 'contact' }">
            <RouterLink to="/contact" class="nav-link">
              <span class="sidebar-icon"><font-awesome-icon :icon="['fas', 'phone']"/></span>
              <span class="sidebar-text"> Contact</span>
            </RouterLink>
          </li> -->
        </ul> 
      </div>
    </nav>
    <div class="content">
      <RouterView />
    </div>
  </div>
</template>


<script setup>

import { RouterLink, RouterView } from 'vue-router'
import { useBankStore } from '@/stores/bank'
import { onMounted } from 'vue'

const store = useBankStore()

onMounted(() => {
  if (store.isLogin) {
    store.getCurrentUser()
  }
})
</script>


<style>
@import url("@/assets/styles/main.css");

.layout {
  display : flex;
}
#sidebarMenu{
  font-family: "Song Myung", sans-serif;
  
}
.sidebar {
  width: 250px;
  height: 100vh;
  position: fixed;
}

.content {
  margin-left: 250px;
  padding: 20px;
  flex-grow: 1;
}

.nav-item {
  cursor: pointer;
}

span {
  font-size: 13pt;
}
</style>