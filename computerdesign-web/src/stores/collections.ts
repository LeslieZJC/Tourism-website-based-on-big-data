import { number } from "echarts"
import { defineStore } from "pinia"
import LocalCache from "@/utils/cache/index"




export const useCollections = defineStore('collections',{
    state:()=>({
        collectionIds:[0]
    }),
    actions:{
        setCollectionIds(collectionIds:number[]){
            this.collectionIds = collectionIds
            console.log(this.collectionIds);

            LocalCache.setCache("collectionIds",this.collectionIds)
            
        },
    }
})