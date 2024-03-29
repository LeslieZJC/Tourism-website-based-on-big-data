<script setup lang="ts">
import router from '@/router';
import { number } from 'echarts';
import { ref,defineProps } from 'vue'

const props = defineProps({
    title:String,
    score:Number,
    squareUrl:String,
    pos:String,
    info:String,
    id:Number,
    risks:String,
    riskstype:String
})

// const routerAction = {
//     goto(){
//         router.push({
//         path:"/details",
//         query:{
//             attractionId:props.id
//         }
//         });
//         setTimeout(function () {
//             window.location.reload();
//         }, 100);
//   }
// }
// console.log("id",props.id);

// const path = "/details?attractionId="+String(props.id)



</script>

<template>
    <div class="main-content">
        <router-link :to="`/details?attractionId=`+String(props.id)" class="left-content">
            <img :src="squareUrl">
        </router-link>

        <router-link :to="`/details?attractionId=`+String(props.id)" class="right-content">
            <div style="font-size: 18px;font-weight: 500;">
            <el-badge :value="risks" :type="riskstype" class="item">
                {{title}}
            </el-badge>
            </div>
            <div>
                  <el-rate
                    v-model="score"
                    disabled
                    show-score
                    text-color="#ff9900"
                    score-template="{value}"
                />

            </div>
            <div style="color: gray;">
                 {{pos}}
            </div>

            <div class="info">
                {{info}}
            </div>

        </router-link>
    </div>
</template>

<style scoped>
a {
    text-decoration: none;
}

.main-content {
    /* height: 70px;*/
    width: 100%; 
    height: 100%;
    background-color:aqua;
    display: flex;
}

.left-content{
    flex: 2;
    /* flex-basis: 208px; */
    background-color: rgb(255, 255, 255);
    padding: 10px;
}

.right-content {
    display: block;
    flex: 8;
    background-color: white;
    padding: 10px;
    color: black;
    font: 14px/1.5 'Microsoft YaHei',arial,tahoma,\5b8b\4f53,sans-serif;
}

.right-content>div {
    text-align: left;
    margin-top: 5px;
    
}

img {
    height: 100%;
    width: 100%;
}

.info {
               /* width: 280px; */
               color: gray;
                text-indent: 2em;
                height: 82px;

                overflow: hidden;

                text-overflow: ellipsis;

                display: -webkit-box;

                -webkit-line-clamp: 4;

                -webkit-box-orient: vertical;
}

.item {
  /* margin-top: 10px;
  margin-left: 40px; */
  /* margin-bottom: 5px; */
}
</style>