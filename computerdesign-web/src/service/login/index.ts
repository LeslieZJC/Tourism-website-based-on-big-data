import axios from "axios";
import request from "../request";





export function login(email:string,password:string){
    return new Promise((resolve,reject)=>{
        request.post("/user/login",{
            email,
            password
        },{
            withCredentials: true
        }).then((res)=>{
            resolve(res)
        })
    })
}

// export function login(email:string,password:string){
//     return axios({
//         method:'post',
//         url:'http://localhost:8888/user/login',
//         data:{
//             email,
//             password
//         }
//     }) 
// }
