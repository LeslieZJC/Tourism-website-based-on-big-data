import {defineStore} from "pinia"
import LocalCache from "@/utils/cache/index"
import { number } from "echarts";
import type { Attract } from '@/service/home/type'


let flag:boolean;
if(LocalCache.getCache("labelVisable")){
    if(LocalCache.getCache("labelVisable")=="false"){
        flag=false
    }else{
        flag=true
    }
    
    // flag = Boolean(LocalCache.getCache("labelVisable")) 
}else{
    flag = true
}


export const useHome = defineStore('home',{
    state:()=>({
        labelVisable:false,
        provinDiagnose: new Map<String,number>(),
        diagnoseCouter:0,
        recommonsAttraction:[]

    }),
    actions:{
        setLabelVisablen(labelVisable:boolean){
            this.labelVisable = labelVisable
            console.log(this.labelVisable);
            
            LocalCache.setCache("labelVisable",this.labelVisable)
        },
        setProvinDiagnose(provinDiagnose:Map<String,number>){
            this.provinDiagnose = provinDiagnose
        },
        setDiagnoseCouter(diagnoseCouter:number){
            this.diagnoseCouter = diagnoseCouter
        },
        setRecommonsAttraction(recommonsAttraction:any){
            this.recommonsAttraction = recommonsAttraction
        },
    }
})
