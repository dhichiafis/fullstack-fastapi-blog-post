
<script setup>
import axios from 'axios'
import { onBeforeMount } from 'vue'
import {RouterView,RouterLink} from 'vue-router'
import {useStore} from 'vuex'
const store=useStore()
onBeforeMount(()=>{
  const token=store.state.token 
  if(token){
    axios.defaults.headers.common['Authorization']='token'+token
  }else{
    axios.defaults.headers.common['Authorization']=''
  }
})
</script>
<template>
  <RouterView></RouterView>
</template>