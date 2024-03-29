<script setup lang="ts">
import { computed, ref } from 'vue'
import SearchAttraction from './SearchAttraction.vue'
import { searchAttracion } from '@/service/search';
import { useRoute } from 'vue-router';
import type { Attract } from '@/service/home/type';


// 获取路由传递的参数并且发axios请求
const route = useRoute()
const keyword = route.query.keyword

// 搜索到的景点
const attractions = ref<Attract[]>([])

//风险地区
const badge = ref("")
const badgetype = ref("")


// 分页
const currentPage = ref(1)
const pageSize = ref(1)
const total = ref(1)

searchAttracion(keyword,1).then((res)=>{
  const data = res.data
  if(res.data.code === 200){
    // console.log(data);
    attractions.value = data.attractions.list
    pageSize.value = data.attractions.pageSize
    total.value = data.attractions.totalCount
    // console.log(attractions.value);

  }
})



const count = ref(20)
const loading = ref(true)
const load = () => {
  loading.value = true
  setTimeout(() => {
    count.value += 2
    loading.value = false
  }, 2000)
}




const small = ref(false)
const background = ref(true)

const handleSizeChange = (val: number) => {
  console.log(`${val} items per page`)
}
const handleCurrentChange = (val: number) => {
  console.log(`current page: ${val}`)
  // 改变分页后重新发送请求
  searchAttracion(keyword,currentPage.value).then((res)=>{
  const data = res.data
  if(res.data.code === 200){
    // console.log(data);
    attractions.value = data.attractions.list
    pageSize.value = data.attractions.pageSize
    total.value = data.attractions.totalCount
    console.log("更改分页后数据",attractions.value);
    
    
  }
})
}
</script>

<template>
    <div v-if="attractions.length===0" style="height: 100%;">
        没有任何匹配的结果哦~
    </div>

    <div v-else style="height: 100%;">

        <div  class="body" >
            <!-- 展示的景点列表 -->
            <div class="infinite-list-wrapper" style="overflow: auto">
                <ul
                    v-infinite-scroll="load"
                    class="list"
                    infinite-scroll-disabled="disabled"
                >

                  <li v-for="(attract,index) in attractions" :key="index" class="list-item">
                    <SearchAttraction
                      v-if="attract.risks==1"
                      :squareUrl="attract.avate" 
                      :title="attract.title"
                      :info="attract.info" 
                      :score="attract.score"
                      :pos="attract.pos"
                      :id="attract.id"
                      risks="高风险"
                      riskstype="danger"
                    >
                    </SearchAttraction>

                    <SearchAttraction
                      v-else
                      :squareUrl="attract.avate" 
                      :title="attract.title"
                      :info="attract.info" 
                      :score="attract.score"
                      :pos="attract.pos"
                      :id="attract.id"
                      risks="安全"
                      riskstype="success"
                    >
                    </SearchAttraction>
                  </li>
                  
                </ul>
            </div>
        </div>

        <div class="footer">
            <div class="pagination-block">
                <el-pagination
                v-model:currentPage="currentPage"
                v-model:page-size="pageSize"
                :small="small"
                :background="background"
                layout="prev, pager, next, jumper"
                :total="total"
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                />
            </div>
         </div>
    </div>

</template>

<style scoped>
.body {
    height: 100%;
    background-color: white;
}

.footer {
    margin-top: 5px;
    
    display: flex;
    justify-content: center;
    /* color: black; */
}

.infinite-list-wrapper {
  height: 100%;
  text-align: center;
}
.infinite-list-wrapper .list {
  padding: 0;
  margin: 0;
  list-style: none;
}

.infinite-list-wrapper .list-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 200px;
  background: var(--el-color-danger-light-9);
  color: var(--el-color-danger);
}
.infinite-list-wrapper .list-item + .list-item {
  margin-top: 10px;
}


</style>