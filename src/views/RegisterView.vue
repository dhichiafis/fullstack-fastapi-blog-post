<script setup>
import authlayout from '../layout/authlayout.vue'
import {reactive} from 'vue'
import axios from 'axios'
import {useRouter,useRoute} from 'vue-router'
const formData=reactive({
    username:'',
    password:''
})
const router=useRouter()
const submit=()=>{
    axios.post('http://localhost:8900/users/new/user',{username:formData.username,password:formData.password}).then(response=>{
        router.push('/login')
    }).catch(error=>{
        console.log(error);
    })
}
</script>
<template>
<authlayout>
    <div class="lg:max-w-md sm:max-w-sm mx-auto mt-7 px-5">
        <form @submit.prevent="submit">
            <div class="flex flex-col">
                <label for="username" class="mb-2 text-gray-600 text-[18px]">username</label>
                <input type="text" v-model="formData.username" class="py-3 px-4 rounded-md border border-gray-400">
            </div>
            <div class="flex flex-col mt-5">
                <label for="password" class="mb-2 text-gray-600 text-[18px]">password</label>
                <input type="password" v-model="formData.password" class="py-3 px-4 rounded-md border border-gray-400">
            </div>
            <div class="mt-5">
                <button type="submit" class="block w-full py-3
                rounded-md text-white bg-gray-900">register</button>
            </div>
        </form>
    </div>
</authlayout>
</template>