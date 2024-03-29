import {defineStore} from "pinia"
import LocalCache from "@/utils/cache/index"


export const useUser = defineStore('user',{
    state:()=>({
        token:LocalCache.getCache("token") ?? ""
    }),
    actions:{
        setToken(token:string){
            this.token = token
            LocalCache.setCache("token",this.token)
        }
    }
})
