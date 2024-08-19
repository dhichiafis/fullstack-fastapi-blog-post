import {createStore} from 'vuex'
const store=createStore({
    state:{
        isAuthenticated:false,
        token:''
    },
    mutations:{
        initializeStore(state){
            if(localStorage.getItem('token')){
                state.isAuthenticated=true 
                state.token=localStorage.getItem('token')
            }else{
                state.isAuthenticated=false 
                state.token=''
            }
        },
        setToken(state,token){
            state.isAuthenticated=true 
            state.token=token 
        },
        removeToken(state){
            state.isAuthenticated=false 
            state.token=''
        }
    }
})

export default store;