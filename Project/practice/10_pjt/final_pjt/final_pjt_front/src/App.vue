<template>
  <SideBar />
</template>


<script setup>
import { useBankStore } from './stores/bank'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';
import SideBar from '@/components/SideBar.vue'

const store = useBankStore()
</script>


<style scoped>
@import './assets/css/volt.css';

</style>