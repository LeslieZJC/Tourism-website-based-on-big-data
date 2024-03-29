<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { getHistory,addHistory } from '@/service/home';
import router from '@/router';

const avatar = "https://thirdwx.qlogo.cn/mmopen/vi_32/WcNZdTpzxFmraykT1HNibHbGM4lRaYhaU4MAwVK9pfIWo0dKwhfEda2DCGb5JDc10IibPF6TVtHD8ZjLJwka684g/132"


interface RestaurantItem {
  value: string
  link: string
}

const state1 = ref('')

const restaurants = ref<RestaurantItem[]>([])
const querySearch = (queryString: string, cb: any) => {
  const results = queryString
    ? restaurants.value.filter(createFilter(queryString))
    : restaurants.value
  cb(results)
}
const createFilter = (queryString: string) => {
  return (restaurant: RestaurantItem) => {
    return (
      restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0
    )
  }
}
const loadAll = async () => {
  const result = ref([{value:"",link:""}]);
  let res = await getHistory()
  const data = res.data
    
  if(data.code==200){
      for(let i in res.data.history) {
        result.value.push({value:res.data.history[i],link:i})
      }
  }
  return result.value;
}
// 定义路由跳转
const routerActions = {
  searchTo(){
    router.push({
      path:"/search",
      query:{
        keyword:state1.value
      }
    });
    setTimeout(function () {
        window.location.reload();
    }, 100);
  }
}




const handleSelect = (item: RestaurantItem) => {
  // console.log("select");
  
  routerActions.searchTo();
}

const handleChange = (text:String) => {
  // console.log("change");
  addHistory(state1.value)
  // console.log(state1.value);
  
  routerActions.searchTo()
}

const searchButton = ()=>{
  addHistory(state1.value)
  routerActions.searchTo()
}


onMounted(async () => {
  restaurants.value = await loadAll();

})



</script>

<template>
    <div class="header">
        <el-avatar style="margin-left: 20px;" :size="50" :src="avatar" />
        <label class="username">Eternity</label>


        <div class="histroy">
            <el-icon class="search" :size="20"><search /></el-icon>
            <el-autocomplete
                v-model="state1"
                :fetch-suggestions="querySearch"
                clearable
                style="width: 400px;"
                placeholder="输入要查询的景点"
                @select="handleSelect"
                @change="handleChange"
            />
            <el-button type="primary" class="search-all" @click="searchButton">查询</el-button>
      </div>
    </div>
</template>

<style scoped>

.search{
    margin-right: 10px;
    margin-top: 0px;
    /* size: 100; */
    vertical-align: middle;
}
.search-all{
  margin-left: 10px;
  width: 50px;
}
.header{
    /* margin-top: 15px; */
    display: flex;
    flex-wrap: nowrap;
    height: 100%;
    
}

.username{
    display: block;
    text-align: center;
    line-height: 50px;
    margin-left: 10px;
    color: black;
}

.histroy {
    /* float: right; */
    position: relative;
    left: 600px;
    top: 15px;
}
</style>