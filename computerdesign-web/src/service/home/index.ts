import axios from "axios";
import type {AxiosResponse} from 'axios'

import request from "../request";



// const instance = axios.create({
//     baseURL: '/nCoV/api'
// })

// 获取所有的标签
export function getAllLabel(){
    return request({
        method:'get',
        url:'/user/login',
    }) 
}



// 获取疫情数据
export function getOutbreakInfo (){
    return new Promise((resolve,reject)=>{
        request.get("https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery34102848205531413024_1584924641755&_=1584924641756",{
            headers:{
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
            }
        })
        .then((res:any)=>{
            resolve(res)
        })
    })
}

// export function getProvinceName (){
//     return new Promise((resolve,reject)=>{
//         axios.get("https://lab.isaaclin.cn/nCoV/api/provinceName",{
//         }).then((res:any)=>{
//             resolve(res)
//         })
//     })
// }

// 请求用户收藏的景点
export function getCollection (){
    return new Promise((resolve,reject)=>{
        request.get("/attraction/collection",{})
        .then((res:any)=>{
            resolve(res)
        })
    })
}


// 获取推荐的景点



// 获取用户的历史搜索记录
export function getHistory (){
    return new Promise<AxiosResponse>((resolve,reject)=>{
        request.get("/attraction/history",{})
        .then((res)=>{
            resolve(res)
        })
    })
}

// 增加用户的历史搜索记录
export function addHistory (keyword:string){
    
    
    return new Promise<AxiosResponse>((resolve,reject)=>{
        console.log("keyword",keyword);
        request.post("/attraction/addhistory/"+keyword)
        .then((res)=>{
            resolve(res)
        })
    })
}


// 随机获取十条景点数据
export function getMHRecommon (){
    return new Promise<AxiosResponse>((resolve,reject)=>{
        request.get("/attraction/recommd",{})
        .then((res)=>{
            resolve(res)
        })
    })
}


// 随机获取十条景点数据 getRealRecommon
export function getRealRecommon(provinces:string,category:string,tags:string[]){
    return new Promise<AxiosResponse>((resolve,reject)=>{
        request.post("/attraction/relrecommd",{
            provinces,
            category,
            tags
        },{
            withCredentials: true
        }).then((res)=>{
            resolve(res)
        })
    })
}
