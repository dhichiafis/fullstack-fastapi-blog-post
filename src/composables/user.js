import {reactive} from 'vue'
import axios from 'axios'
import store from '../store'
export function useUser(){
    let user=reactive({
        username:'',
        password:'',
        id:0
    })

    async function getUser(){
        const access_token=store.state.token 
        await axios.get('http://localhost:8900/users/users/me/',
            {headers:{
                'ContentType':'application/json',
                Authorization:`Bearer ${access_token}`
            }}
        ).then(response=>{
            user=response.data 
            console.log(user);
        })
    }
    return {user,getUser}
}