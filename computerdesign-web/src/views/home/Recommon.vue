<script setup lang="ts">
import { getCollection,getMHRecommon } from '@/service/home';
import type { Attract } from '@/service/home/type'
import { useCollections } from '@/stores/collections';
import { useHome } from '@/stores/home';

import { ref, watch } from 'vue';
import Attraction from './Attraction.vue';

const collections = ref<Attract[]>([])
// 请求用户收藏的景点
getCollection().then((res:any)=>{
  // console.log(res.data);
  const data = res.data
  if(data.code == 200){
    collections.value = data.collection
    // console.log(collections);
  }

})

// 推荐的景点
const recommonsAttraction = ref<Attract[]>([])

function getMoHuRecommon(){
  getMHRecommon().then((res)=>{
      const data = res.data
      if(data.code == 200){
        recommonsAttraction.value = data.Recommd
        // console.log(collections);
      }
  })
}
getMoHuRecommon()

// 准确推荐景点
const home = useHome()
function getReakRecommon(){
  // 弹出选择标签
  home.setLabelVisablen(true)
  
}
// 如果LabelVisablen发生变化就更新从pinna中拿数据
watch(() => home.$state.recommonsAttraction, (newValue, oldValue) => {
  // recommonsAttraction.value = home.$state.recommonsAttraction
  // console.log("pinna中数据发生变化",newValue);
  recommonsAttraction.value = home.$state.recommonsAttraction
  
    
})



</script>

<template>
    <div class="aside-content">
      <div>
          <el-card class="box-card-1">
            <template #header>
            <div class="card-header">
                <span>推荐景点</span>
                <div>
                  <el-button class="button" type="text" @click="getMoHuRecommon">模糊推荐</el-button>
                  <el-button class="button" type="text" @click="getReakRecommon">精确推荐</el-button>
                </div>

            </div>
            </template>
            <Attraction v-for="(collect,index) in recommonsAttraction" :key="index" 
            :avater="collect.avate" 
            :title="collect.title"
            :introduce="collect.info" 
            :id="collect.id"
            class="text">
            </Attraction>

        </el-card>
      </div>


      <div>
        <el-card class="box-card-1">
            <template #header>
            <div>
                <span>收藏景点</span>
            </div>
            </template>
            <Attraction v-for="(collect,index) in collections" :key="index" 
            :avater="collect.avate" 
            :title="collect.title"
            :introduce="collect.info" 
            :id="collect.id"
            class="text">
            </Attraction>
        </el-card>
      </div>



  </div>
</template>

<style scoped>
.aside-content{
    width: 90%;
    margin: 0 auto;
    display: flex;
    height: 100%;
    flex-direction: column;
}

.aside-content>div:nth-child(1) {
    flex: 0 0  550px;
    padding: 2%;
    height: 100%;
      overflow: hidden;
}
.aside-content>div:nth-child(2) {
    flex: 0 0 320px;
    /* background-color: antiquewhite; */
    padding: 2%;
    padding-top: 5%;
    height: 100%;
      overflow: hidden;
}

.box-card-1 {
  height: 100%;
  background-color: rgb(255, 252, 252);
  border-color: black;
  color: rgb(0, 0, 0);
  /* padding: 2%; */
  overflow: auto;
}

.box-card-2 {
  /* height: 100%; */
  background-color: rgb(36, 34, 34);
  border-color: black;
  color: white;
}


 .card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}



.text {
  font-size: 14px;
}

.item {
  margin-bottom: 30px;
} 

</style>