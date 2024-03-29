<script setup lang="ts">
import { number } from 'echarts';
import { ref, defineProps, watch } from 'vue';
import { recommndById } from '@/service/details';
import type { Attract } from '@/service/home/type';
const prop = defineProps({
    attractionId:Number
})
const activeName = ref('info')

// 发送axios请求去根据id推荐景点
// 得到的景点
const attractions = ref<Attract[]>([])
function getData(){
    recommndById(Number(prop.attractionId)).then((res)=>{
        console.log(res.data);
        const data = res.data
        if(data.code == 200){
            attractions.value = res.data.attractions
            console.log(attractions.value);
            
        }
    })
}
getData()
watch(() => prop.attractionId, (newValue, oldValue) => {
    getData()
    
})



</script>

<template>
            <div>
                <el-tabs
                    v-model="activeName"
                    type="card"
                    class="demo-tabs"
                >
                    <el-tab-pane label="推荐" name="info">
                        
                            <div class="img-card">
                                <div 
                                v-for="(item,index) in attractions"
                                :key="index"
                                >
                                    <router-link :to="`/details?attractionId=`+String(item.id)" class="attraction">
                                    <img :src="item.avate">
                                    <div>
                                        {{item.title}}
                                    </div>
                                    </router-link>
                                </div>
                            </div>
                    </el-tab-pane>
                </el-tabs>
            </div>
</template>

<style scoped>
.img-card {
    width: 100%;
    height: 300px;
    /* background-color: rgb(0, 0, 0); */
    display: flex;
}
.img-card >div{
    flex: 1;
    padding: 10px;
}



 img {
    width: 100%;
    height: 75%;
}

.img-card >div div {
    text-align: center;
    line-height: 90px;
    font-size: 30px;
    font-weight: 600;
    font-family: Helvetica, 'Hiragino Sans GB', 'Microsoft Yahei', '微软雅黑', Arial, sans-serif;
    color: rgb(36, 33, 33);
}

a {
    text-decoration: none;
}

</style>