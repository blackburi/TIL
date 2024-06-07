<template>
  <h1>환율 정보</h1>
  <hr>
  <div class="py-4 bg-light">
    <div class="row mx-3">
      <div class="col-12">
        <div>

          <h3>외화로 환전</h3>
          <p>한화 ⇒ 외화</p>

          <div class="input-group mb-3" style="height: 70px;">
            <select class="form-select form-select-sm" name="외화" id="foreign" v-model="selectedForeign" style="width: 20%;">
              <option value="" selected>국가/통화</option>
              <option v-for="exchange in exchanges" :key="exchange.cur_unit" :value="exchange.cur_unit">
                {{ exchange.cur_unit }} - {{ exchange.cur_nm }}
              </option>
            </select>
          <input class="form-control" type="text" id="beforeWon" v-model.trim="beforeWon" style="width: 80%;">
          <br>
          <p v-if="selectedExchange">
            {{ selectedExchange.cur_nm }} : {{ calculateToForeign() }}
          </p>
        </div>
        <hr>
        <div>
          <h3>한화로 환전</h3>
          <p>외화 ⇒ 한화</p>
          <div class="input-group mb-3" style="height: 70px;">
            <select class="form-select form-select-sm" name="외화" id="foreignToWon" v-model="selectedForeignToWon" style="width: 20%;">
              <option value="" selected>국가/통화</option>
              <option v-for="exchange in exchanges" :key="exchange.cur_unit" :value="exchange.cur_unit">
                {{ exchange.cur_unit }} - {{ exchange.cur_nm }}
              </option>
            </select>
            <input class="form-control" type="text" id="beforeForeign" v-model.trim="beforeForeign" style="width: 80%;">
            <br>
            <p v-if="selectedExchangeToWon">
              한화 : {{ calculateToWon() }} (원)
            </p>
          </div>
        </div>
      </div>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios'

export default {
  data() {
    return {
      exchanges: null,
      selectedForeign: '',
      selectedForeignToWon: '',
      selectedExchange: null,
      selectedExchangeToWon: null,
      beforeWon: 0,
      beforeForeign: 0,
      calculatedWon : 0,
      calculatedForeign: 0,
    };
  },
  mounted() {
    this.get_exchange_rate();
  },
  methods: {
    async get_exchange_rate() {
      try {
        const response = await axios.get('http://localhost:8000/api/get_exchange_rate/')
        this.exchanges = response.data;
      } catch (error) {
        console.error('Error getting exchange rate data:', error)
      }
    },
    calculateToForeign() {
      if (!this.beforeWon || !this.selectedExchange || !this.selectedExchange.tts) {
        return '값을 입력해 주세요!'
      }
      const tts = parseFloat(this.selectedExchange.tts.replace(/,/g, ''))
      const result = parseFloat(this.beforeWon) / tts;
      this.calculatedForeign = result.toFixed(2)
      return result.toFixed(2)
    },
    calculateToWon() {
      if (!this.beforeForeign || !this.selectedExchangeToWon || !this.selectedExchangeToWon.ttb) {
        return '값을 입력해 주세요!'
      }
      const ttb = parseFloat(this.selectedExchangeToWon.ttb.replace(/,/g, ''))
      const result = parseFloat(this.beforeForeign) * ttb
      this.calculatedWon = result.toFixed(0)
      return result.toFixed(0)
    }
  },
  watch: {
    selectedForeign(newValue) {
      this.selectedExchange = this.exchanges.find(exchange => exchange.cur_unit === newValue);
    },
    selectedForeignToWon(newValue) {
      this.selectedExchangeToWon = this.exchanges.find(exchange => exchange.cur_unit === newValue);
    },
  },
}
</script>


<style scoped>
pre {
  background-color: #f8f9fa;
  padding: 15px;
  border-radius: 5px;
  border: 1px solid #dee2e6;
  color: 1px solid black;
  overflow: auto;
}
</style>