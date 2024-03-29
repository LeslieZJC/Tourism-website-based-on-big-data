<script setup lang="ts">
import { ref,computed } from 'vue';
import { useHome } from '@/stores/home';
import { number } from 'echarts';

// 设置当前时间
const currentTime = ref("")

setInterval(function() {   
    let time = new Date();   // 程序计时的月从0开始取值后+1   
    let m = time.getMonth() + 1;   
    currentTime.value = time.getFullYear() + "-" + m + "-"     
    + time.getDate() + " " + time.getHours() + ":"     
    + time.getMinutes() + ":" + time.getSeconds();   
}, 1000); 

// 监听pinia，获取各个省份疫情信息
const home = useHome()
const provinDiagnose = computed(()=>home.provinDiagnose)

const diagnoseCouter = computed(()=>home.diagnoseCouter)





</script>

<template>
    <div class="aside">
        <div class="all-diagnose ">
            <!-- <el-card shadow="hover"> Hover </el-card> -->
            <el-card shadow="hover" class="box-card text">
                <div style="font-size: 20px;font-weight: 600; margin-top: 10%;">全国累计确诊人数</div>
                <div style="font-size: 40px;font-weight: 600;margin-top: 5%;color: rebeccapurple;">{{diagnoseCouter}}</div>
            </el-card>

        </div>

        <div class="detailed-diagnose" style="overflow: hidden;">
            <el-card class="box-card">

                <div v-for="(item,key) in provinDiagnose" class="text item" :key="key">
                    <p v-for="(value,index) in item" :key="index" style="display: inline;margin-left: 10px;color: black">
                        <!-- {{item[index]}} -->
                        {{value}}
                    </p>
                </div>


            </el-card>
        </div>

        <div class="footer-time">
            <el-card  class="box-card text"> 
                <div>当前时间（实时更新）</div>
                <div>{{currentTime}}</div>
            </el-card>
        </div>
    </div>



</template>

<style  scoped>
.text {
  font-size: 20px;
  font-weight: 600;
  color: rgb(0, 0, 0);
}

.item {
  padding: 5px 0;
}

.aside {
    display: flex;
    flex-direction: column;
    height: 100%;
}
.all-diagnose {
    flex: 2;
    /* background-color: aliceblue; */
    padding: 10px;

}

.all-diagnose div {
    text-align: center;
}

.detailed-diagnose{
    /* flex-basis: 588px; */
    flex: 0 0 588px;
    flex-grow: 0;
    /* background-color: aqua; */
    padding: 10px;
}

.footer-time {
    flex: 1;
    /* background-color: bisque; */
    padding: 10px;
    text-align: center;
}

.box-card {
    height: 100%;
    background-color: rgb(255, 255, 255);
    border-color: rgb(110, 108, 108);
    overflow: auto;
}

</style>
