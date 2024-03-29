import type { AxiosResponse } from "axios"
import request from "../request"



// 获取用户的历史搜索记录
export function searchAttracion (keyword:any,currentPage:Number){
    return new Promise<AxiosResponse>((resolve,reject)=>{
        request.get("/attraction/search"+"?keyword="+keyword+"&currentPage="+currentPage,{})
        .then((res)=>{
            resolve(res)
        })
    })
}