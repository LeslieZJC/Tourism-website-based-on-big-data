import type { AxiosResponse } from "axios"
import request from "../request"



export function getDetails (attractionId:number){
    return new Promise<AxiosResponse>((resolve,reject)=>{
        request.get("/attraction/details?attractionId="+attractionId,{})
        .then((res)=>{
            resolve(res)
        })
    })
}

export function getComment (attractionId:number,currentPage:number){
    return new Promise<AxiosResponse>((resolve,reject)=>{
        request.get("/attraction/comments?attractionId="+attractionId+"&currentPage="+currentPage,{})
        .then((res)=>{
            resolve(res)
        })
    })
}


export function getLable (attractionId:number){
    return new Promise<AxiosResponse>((resolve,reject)=>{
        request.get("/attraction/label?attractionId="+attractionId,{})
        .then((res)=>{
            resolve(res)
        })
    })
}



// 发送收藏的请求
export function addCollect (attractionId:number){
    return new Promise<AxiosResponse>((resolve,reject)=>{
        request.post("/attraction/addcollect/"+String(attractionId))
        .then((res)=>{
            resolve(res)
        })
    })
}

// 取消收藏的请求
export function disCollect (attractionId:number){
    return new Promise<AxiosResponse>((resolve,reject)=>{
        request.delete("/attraction/discollect/"+String(attractionId))
        .then((res)=>{
            resolve(res)
        })
    })
}


// 发送收藏的请求
export function recommndById (attractionId:number){
    return new Promise<AxiosResponse>((resolve,reject)=>{
        request.get("/attraction/recommndById/"+String(attractionId))
        .then((res)=>{
            resolve(res)
        })
    })
}
