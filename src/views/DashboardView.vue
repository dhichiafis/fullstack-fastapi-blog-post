<script  setup>
import dashlayout from '../layout/dashlayout.vue'
import axios from 'axios'
import {useUser} from '../composables/user'
import { useStore } from 'vuex'
import {useRouter} from 'vue-router'
import { computed, onBeforeMount } from 'vue'
const store=useStore()
const {user,getUser} = useUser()
const userinfo=computed(()=>{
  return user   
})
const router=useRouter()
const blogs=[
    {
        'title':'this is the first blog',
        'description':'this is the description of the first blog and it imparessive'
    },
    {
        'title':'this is the first blog',
        'description':'this is the description of the first blog and it imparessive'
    },
    {
        'title':'this is the first blog',
        'description':'this is the description of the first blog and it imparessive'
    },
    {
        'title':'this is the first blog',
        'description':'this is the description of the first blog and it imparessive'
    },
    {
        'title':'this is the first blog',
        'description':'this is the description of the first blog and it imparessive'
    },
    {
        'title':'this is the first blog',
        'description':'this is the description of the first blog and it imparessive'
    },
    {
        'title':'this is the first blog',
        'description':'this is the description of the first blog and it imparessive'
    },
    {
        'title':'this is the first blog',
        'description':'this is the description of the first blog and it imparessive'
    },
]
const formData={
    title:'',
    description:''
}
const submit=()=>{
    axios.post('http://localhost:8900/blogs/new/blog?blog_owner=2',
    {title:formData.title,description:formData.description},{
        headers:{
            'Content-Type':'application/json'
        }
    }).then(response=>{
        router.push('/dashboard')
    })
}
onBeforeMount(()=>{
    getUser()
})

</script>
<template>
    <dashlayout>
        <div class="grid lg:grid-cols-[60%,40%] 
        sm:grid-cols-1 space-x-12 px-6 py-12">
            <div>
                <h2 class="font-bold text-[40px]">welcome to the dashboard list of bologs</h2>
                <div class="grid lg:grid-cols-2 gap-x-4 gap-y-4 sm:grid-cols-1">
                    <div v-for="blog in blogs" 
                    class="shadow-md py-3 px-4 sm:max-w-full">
                        <h3 class="text-[22px] font-medium text-left mb-2">{{ blog.title }}</h3>
                        <p class="text-[18px] text-left leading-[1.5]">{{ blog.description }}</p>
                    </div>
                </div>
            
            </div>
            <div class="lg:min-w-md sm:max-w-full mt-9 px-3  mx-4">
                <form @submit.prevent="submit">
                    <div class="flex flex-col">
                <label for="title" 
                class="mb-2 text-gray-600 text-[18px]">title</label>
                <input type="text" v-model="formData.title" class="py-3 px-4 rounded-md border border-gray-400">
            </div>
            <div class="flex flex-col mt-5">
                <label for="descripition" 
                class="mb-2 text-gray-600 text-[18px]">description</label>
                <textarea type="text"
                 v-model="formData.description"
                  class="py-3 px-4 rounded-md border border-gray-400"></textarea>
            </div>
            <div class="mt-5">
                <button type="submit" class="block w-full py-3
                rounded-md text-white bg-gray-900">create blog</button>
                <p @click="router.push('/register')" class="mt-3 text-gray-900"></p>
            </div>
                </form>    
            </div>
            
     </div>
    </dashlayout>
</template>