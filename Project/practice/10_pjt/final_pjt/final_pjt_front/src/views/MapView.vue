<template>
  <h1>주변 은행 검색</h1>
  <hr>
  <!-- <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center py-4 bg-light"> -->

    <div class="row">
      <div class="col-12">
        <div class="card border-light shadow-sm ">
          <div class="card-body bg-light" style="width: 100%;">
            <!-- selectbar start  -->
            <div class="d-flex justify-content-center mb-2" style="height:100px ">
              <div class="row">
                <div class="col align-self-center">
                  <select name="city" id="city" v-model="city" class="form-select select" aria-label="시">
                    <option value="" selected disabled>시/도</option>
                    <option v-for="city of cities" :key="city" :value="city">{{ city }}</option>
                  </select>
                </div>
                <div class="col align-self-center">
                  <select name="area" id="area" v-model="selectedRegion" class="form-select select" aria-label="구">
                    <option value="" selected disabled>시/군/구</option>
                    <option v-for="region of regions" :key="region" :value="region">{{ region }}</option>
                  </select>
                </div>
                <div class="col align-self-center">
                  <select name="bankname" id="bankname" v-model="selectedBank" class="form-select select" aria-label="은행">
                    <option value="" selected disabled>은행</option>
                    <option v-for="bank of banks" :key="bank" :value="bank">{{ bank }}</option>
                  </select>
                </div>
                <div class="col align-self-center">
                  <input type="button" class="btn btn-secondary ml-3" value="검색"  @click="searchPlaces" />
                </div>
              </div>
            </div>
            <div id="map" class="col" style=" width:100%; height: 550px"></div>
            <hr>
            <ul>
              <li v-for="place in places" :key="place.id">{{ place.place_name }}</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  <!-- </div> -->
</template>

<script setup>
import { ref, onMounted, watch } from "vue";

const banks = ref(['경남은행', '광주은행', '국민은행', '기업은행', '농협은행', '대구은행', '부산은행', '산업은행', '수협은행', '신한은행', '우리은행', '전북은행', '제일은행', '제주은행', '카카오뱅크', '케이뱅크', '토스뱅크', '하나은행'])
const cities = ref(["서울특별시", "부산광역시", "대구광역시", "인천광역시", "광주광역시", "대전광역시", "울산광역시", "세종특별자치시", "경기도", "강원특별자치도", "충청북도", "충청남도", "전북특별자치도", "전라남도", "경상북도", "경상남도", "제주특별자치도"])
const regions = ref([])
const city = ref("")
const selectedBank = ref("")
const selectedRegion = ref("")
const places = ref([])
let map

const initializeMap = () => {
  const container = document.getElementById("map");
  const options = {
    center: new kakao.maps.LatLng(37.5665, 126.978), // 서울 중심 좌표
    level: 3,
  }
  map = new kakao.maps.Map(container, options)
}

// 수정된 부분: city의 변경을 감시하여 해당하는 지역 정보를 설정합니다
watch(city, (newVal, oldVal) => {
  console.log('city changed from', oldVal, 'to', newVal)
  switch (newVal) {
  // 해당 도시에 맞는 지역 정보 설정
    case "서울특별시":
      regions.value = ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구"]
      break
    case "부산광역시":
      regions.value = ['강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구']
      break
    case "대구광역시":
      regions.value = ['군위군', '남구', '달서구', '달성군', '동구', '북구', '서구', '수성구', '중구']
      break
    case "인천광역시":
      regions.value = ['강화군', '계양구', '남동구', '동구', '미추홀구', '부평구', '서구', '연수구', '옹진군', '중구']
      break
    case "광주광역시":
      regions.value = ["광산구", "남구", "동구", "북구", "서구"]
      break
    case "대전광역시":
      regions.value = ["대덕구", "서구", "유성구", "중구"]
      break
    case "울산광역시":
      regions.value = ["남구", "동구", "북구", "서구", "울주군"]
      break
    case "세종특별자치시":
      regions.value = ['고운동', '금남면', '나성동', '다정동', '대평동', '도담동', '반곡동', '보람동', '부강면', '새롬동', '소담동', '소정면', '아름동', '어진동', '연기면', '연동면', '연서면', '장군면', '전동면', '전의면', '조치원읍', '종촌동', '한솔동', '해밀동']
      break
    case "경기도":
      regions.value = ['가평군', '고양시 덕양구', '고양시 일산동구', '고양시 일산서구', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시', '부천시 소사구', '부천시 오정구', '부천시 원미구', '성남시 분당구', '성남시 수정구', '성남시 중원구', '수원시 권선구', '수원시 영통구', '수원시 장안구', '수원시 팔달구', '시흥시', '안산시 단원구', '안산시 상록구', '안성시', '안양시 동안구', '안양시 만안구', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시 기흥구', '용인시 수지구', '용인시 처인구', '의왕시', '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시']
      break
    case "강원특별자치도":
      regions.value = ['강릉시', '고성군', '동해시', '삼척시', '속초시', '양구군', '양양군', '영월군', '원주시', '인제군', '정선군', '철원군', '춘천시', '태백시', '평창군', '홍천군', '화천군', '횡성군']
      break
    case "충청북도":
      regions.value = ['괴산군', '단양군', '보은군', '영동군', '옥천군', '음성군', '제천시', '증평군', '진천군', '청주시 상당구', '청주시 서원구', '청주시 청원구', '청주시 흥덕구', '충주시']
      break
    case "충청남도":
      regions.value = ['계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시', '예산군', '천안시 동남구', '천안시 서북구', '청양군', '태안군', '홍성군']
      break
    case "전북특별자치도":
      regions.value = ['고창군', '군산시', '김제시', '남원시', '무주군', '부안군', '순창군', '완주군', '익산시', '임실군', '장수군', '전주시 덕진구', '전주시 완산구', '정읍시', '진안군']
      break
    case "전라남도":
      regions.value = ['강진군', '고흥군', '곡성군', '광양시', '구례군', '나주시', '담양군', '목포시', '무안군', '보성군', '순천시', '신안군', '여수시', '영광군', '영암군', '완도군', '장성군', '장흥군', '진도군', '함평군', '해남군', '화순군']
      break
    case "경상북도":
      regions.value = ['경산시', '경주시', '고령군', '구미시', '김천시', '문경시', '봉화군', '상주시', '성주군', '안동시', '영덕군', '영양군', '영주시', '영천시', '예천군', '울릉군', '울진군', '의성군', '청도군', '청송군', '칠곡군', '포항시 남구', '포항시 북구']
      break
    case "경상남도":
      regions.value = ['거제시', '거창군', '고성군', '김해시', '남해군', '밀양시', '사천시', '산청군', '양산시', '의령군', '진주시', '창녕군', '창원시 마산합포구', '창원시 마산회원구', '창원시 성산구', '창원시 의창구', '창원시 진해구', '통영시', '하동군', '함안군', '함양군', '합천군']
      break
    case "제주특별자치도":
      regions.value = ['제주시', '서귀포시']
      break
    default:
      regions.value = []
  }
})

const searchPlaces = () => {
  if (!selectedBank.value || !selectedRegion.value) {
    alert("지역 또는 은행을 선택해주세요")
    return
  }

  const query = `${selectedBank.value} ${selectedRegion.value}`;

  if (
    typeof kakao === "undefined" ||
    typeof kakao.maps === "undefined" ||
    typeof kakao.maps.services === "undefined"
  ) {
    console.error("Kakao Maps API is not loaded yet.")
    return
  }

  const ps = new kakao.maps.services.Places();
  ps.keywordSearch(query, (data, status, pagination) => {
    if (status === kakao.maps.services.Status.OK) {
      places.value = data
      displayPlaces(data)
    } else {
      alert("검색 결과가 없습니다!")
    }
  });
};

const displayPlaces = (places) => {
  const bounds = new kakao.maps.LatLngBounds();
  for (let i = 0; i < places.length; i++) {
    const place = places[i]
    const markerPosition = new kakao.maps.LatLng(place.y, place.x);
    const marker = new kakao.maps.Marker({
      position: markerPosition,
    });
    marker.setMap(map)
    bounds.extend(markerPosition)
  }
  map.setBounds(bounds)
}

onMounted(() => {
  if (typeof kakao !== "undefined" && kakao.maps) {
    initializeMap()
  } else {
    console.error("Kakao Maps API failed to load.")
  }
})
</script>

<style scoped>
#map {
  width: 500px;
  height: 400px;
}
.card {
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #ddd;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

</style>