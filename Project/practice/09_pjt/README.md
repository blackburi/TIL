# PJT 08

### 이번 pjt 를 통해 배운 내용

* 동영상 검색 관리 서비스 구현

## A. 동영상 검색 결과 출력

* 요구 사항
  * 네비게이션 바에서 Search 링크 클릭
  * 원하는 검색어 입력
  * YouTube API로부터 JSON 데이터 요청
  * 동영상 목록 출력


* 결과
  
  ```html
  <template>
    <div class="container mt-5">
      <h1>동영상 목록 페이지</h1>
      <div class="row">
        <div v-for="video of store.videos.items" :key="video.id.videoId" class="col-lg-4 col-md-6 col-sm-12 mb-4">
          <VideoDetail :video="video" />
        </div>
      </div>
    </div>
    <RouterView />
  </template>


  <script setup>
  import VideoDetail from '@/components/VideoDetail.vue'
  import { RouterLink, RouterView } from 'vue-router'
  import { useVideosStore } from '@/stores/videos'
  const store = useVideosStore()
  </script>
  ```
  
  * 이 문제에서 어려웠던점
    * 원하는 검색어 입력을 통해 원하는 JSON 데이터 요청을 하고 동영상 목록을 출력하는 것
  * 내가 생각하는 이 문제의 포인트 
    * 입력값을 통해 관련된 동영상 데이터를 가져올 때 입력값을 어떻게 전달해 줄 것인지가 포인트였다.

-----

## B. 동영상 상세 정보 출력

* 요구 사항
  * 검색결과에서 특정 비디오 클릭
  * 동영상에 대한 상세 정보 출력
  * iframe 태그 활용해 동영상 재생
  * 동영상 저장
    * Local Storage 활용
    * 저장 안 된 동영상 => 동영상 저장 버튼
    * 저장된 동영상 => 저장 취소 버튼


* 결과
  
  ```html
  <template>
    <div class="container mt-5">
      <h1>상세 정보</h1>
      <hr>
      <h3>{{ video.snippet.title }}</h3>
      <iframe id="player" type="text/html" width="640" height="360"
      :src="'http://www.youtube.com/embed/' + videoId + '?enablejsapi=1&origin=http://example.com'"
    frameborder="0">
      </iframe>
      <hr>
      <p>Description : {{ video.snippet.description }}</p>
      <button @click="store.later(videoId)" class="btn">
        <span v-if="store.laterVideos.includes(videoId)">❤️</span>
        <span v-else>🤍</span>
      </button>
    </div>
  </template>


  <script setup>
  import { useVideosStore } from '@/stores/videos'
  import { useRoute, useRouter } from 'vue-router'

  const route = useRoute()
  const videoId = route.params.videoId

  const store = useVideosStore()
  const video = store.videos.items.find((element) => element.id.videoId === videoId)
  </script> 
  ```
  
  * 이 문제에서 어려웠던점
    * iframe을 처음 이용하여 사용법을 잘 몰라서 detail에 들어갔을 때 동영상을 재생시킬수 있는 방법을 찾아서 활용하는 것이 어려웠다.
  * 내가 생각하는 이 문제의 포인트
    * iframe을 이해하고 실행하는 것이 포인트였다.

-----

## C. 나중에 볼 동영상 저장 및 삭제

* 요구 사항
  * 저장된 동영상 목록 확인
    * Local Storage 활용
    * 등록된 동영상 없을 경우 - 등록된 비디오 없음 출력

* 결과 : 
  
  ```html
  <template>
    <div class="container mt-5">
      <h1>저장한 동영상</h1>
      <div class="row" v-if="store.laterVideosList.length">
        <div v-for="video of store.laterVideosList" class="col-lg-4 col-md-6 col-sm-12 mb-4">
          <div class="card" style="width: 18rem;">
            <p class="card-text text-center">{{ video.title }}</p>
            <img :src="video.snippet.thumbnails.high.url" class="card-img-top" alt="#" style="width: 100%; height: 200px;">
            <div class="card-body">
              <button @click="store.later(video.id.videoId)" class="btn">
                <span v-if="store.laterVideos.includes(video.id.videoId)">❤️</span>
                <span v-else>🤍</span>
              </button>
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        <p>등록된 비디오 없음</p>
      </div>
    </div>
  </template>


  <script setup>
  import { useVideosStore } from '@/stores/videos'
  import { useRoute, useRouter, onBeforeRouteUpdate } from 'vue-router'

  const route = useRoute()
  const videoId = route.params.videoId

  const store = useVideosStore()
  </script>
  ```
  ```js
  import { computed, ref } from 'vue'
  import { defineStore } from "pinia"
  import axios, { all } from 'axios'

  // const API_KEY = 'AIzaSyC31xwCxkurrC1VbdCYM9IU71Xv51LR4u0'
  const API_KEY = 'AIzaSyD4CRDN86DBeLUKLUv06bACLVtmXVJ-VCQ'
  const API_URL = 'https://www.googleapis.com/youtube/v3/search'

  export const useVideosStore = defineStore('videos', () => {
    const videos = ref([])
    const laterVideos = ref([])
    const query = ref('ssafy')
    const fetchVideo = ((query) => {
      axios({
        method: 'get',
        url: API_URL,
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: query.value,
          maxResults: 50
        },
      }).then((response) => {
        videos.value = response.data
      }).catch((error) => {
        console.log(error)
      })

    })


    const findVideo = function (id) {
      const video = videos.value.items.find((element) => element.id.videoId === id)
      return video
    }


    const later = function (videoId) {
      if (laterVideos.value.includes(videoId)) {
        const Index = laterVideos.value.findIndex((id) => id === videoId)
        laterVideos.value.splice(Index, 1)
      } else {
        laterVideos.value.push(videoId)
      }
    }


    const laterVideosList = computed(() => {
      const laters = videos.value.items.filter((video) => laterVideos.value.includes(video.id.videoId))
      return laters
    })


    return { query, fetchVideo, videos, findVideo, laterVideos, laterVideosList, later }
  }, { persist: true })
  ```
  
  * 이 문제에서 어려웠던점
    * 없음
  * 내가 생각하는 이 문제의 포인트
    * `video.js`를 통해 원하는 데이터만을 새로 만들어 그 데이터를 이용하여 출력하는 것이 포인트였다.

-----


# 후기
* backend를 이용하지 않고 frontend만을 이용하여 웹 서비스를 구현하는 것도 재밌었다.