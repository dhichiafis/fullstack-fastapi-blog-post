import {createRouter,createWebHistory} from 'vue-router'
import store from '../store'
const routes=[
    {
        path:'/',
        name:'home',
        component:()=>import('../views/HomeView.vue')
    },
    {
        path:'/login',
        name:'login',
        component:()=>import('../views/loginView.vue')
    },
    {
        path:'/register',
        name:'register',
        component:()=>import('../views/RegisterView.vue')
    },
    {
        path:'/dashboard',
        name:'dashboard',
        component:()=>import('../views/DashboardView.vue'),
        meta:{
            requiredLogin:true
        }
    }
]
const router=createRouter({
    history:createWebHistory(),
    routes
})
router.beforeEach((to,from,next)=>{
    if(to.matched.some(record=>record.meta.requiredLogin) && !store.state.isAuthenticated){
        next('/login')
    }else{
        next()
    }
})
export default router;