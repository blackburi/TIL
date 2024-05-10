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