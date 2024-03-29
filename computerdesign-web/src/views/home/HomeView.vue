<script setup lang="ts">
// import LabelDialogVue from './LabelDialog.vue';
import request from "@/service/request";

// 导入 echrats 包
import * as echarts from "echarts";
import { ref, onMounted, watch } from "vue";
import axios from "axios";

import { useHome } from "@/stores/home";

// pinia 
const home = useHome()

// 获取dom
const mapDom: any = ref(null);


// 获取地图的数据
let mapData: any = ref([]);
// 下一级地图的id
const childrenId: any = ref("100000");
// 存一次疫情的地图
const mapEpidemic: any = ref([]);
// 获取传过的数据
onMounted(() => {
  // 初始化画布
  var map = echarts.init(mapDom.value);
  // 画布的点击事件 点击进行请求
  map.on("click", function (res: any) {
    // 这个是出自 地图子级的id
    // console.log(mapData.value);
    // let abcode = mapData.value.features.find(
    //   (item: any) => item.properties.name == res.name
    // );
    // // 拿到子级区的id 在下面的axios 进行请求
    // let dataCity = abcode.properties.adcode;
    // childrenId.value = dataCity;
    // // 获取疫情地图 区级的数据
    // let EpidemicData = mapEpidemic.value.find((value: any) => {
    //   return value.value == res.value;
    // });
    // // 请求地图的数据 以及疫情的数据
    // axios
    //   .get(
    //     `https://geo.datav.aliyun.com/areas_v3/bound/${childrenId.value}_full.json`
    //   )
    //   .then((res: any) => {
    //     // registerMap 注册一个地图   mapData 地图的数据包 根据不同的数据渲染不同的地图
    //     console.log(res.data);
        
    //     echarts.registerMap("china", res.data);
    //     // 这个调用是进行地图的渲染 然后把 子级的地图数据传进去 因为如果名字 和 疫情的名字对不上就去不会改变
    //     map.setOption(mapRender(EpidemicData.city, res.data.features));
    //   });
  });

  


  // 首次 请求地图的总数据数据 用来初始化数据
  request
    .get(`/map/aliyun`)
    .then((res: any) => {
      // console.log(res);
      console.log("地图https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json的总数据",res.data);
      
      // 存一次数据 用来找子级
      mapData.value = res.data;
      // registerMap 注册一个地图   mapData 地图的数据包 根据不同的数据渲染不同的地图
      echarts.registerMap("china", res.data.body);
      // 这个调用是进行地图的渲染
      mapRender();
    });
  // 首次 请求疫情的数据 因为接口 设计到跨域 所以要进行 proxy 进行代理
  request
    .get("/map/sina")
    .then((res: any) => {
      // 将数据备份一次 用来查找子级
      // console.log(res);
      console.log("/api/news/wap/fymap2020_data.d.json?_=1580892522427接口数据",res.data);
      
      
      mapEpidemic.value = res.data.body.data.list;
      // 这个调用是疫情数据的渲染  mapRender 处理数据的函数
      let data = mapRender(res.data.body.data.list);
      // option 数据传入进去 设置数据
      map.setOption(data);
    });
});
// 处理数据的函数 以及 echarts 的option 数据配置 这个函数非常重要
const mapRender = (data: any = [], mapData: any = []) => {
  let mapLocal: any = [];
  mapData.forEach((value: any, index: number) => {
    // console.log(value.properties.name);
    mapLocal.push(value.properties.name);
  });
  let city = ["北京", "重庆", "上海", "天津"];
  let area: any = {
    内蒙古: "内蒙古自治区",
    新疆: "新疆维吾尔自治区",
    广西: "广西壮族自治区",
    宁夏: "宁夏回族自治区",
    西藏: "西藏自治区",
    澳门: "俺们特别行政区",
    香港: "香港特别行政区",
  };

  let provinDiagnose = new Map<String,number>();
  let diagnoseCouter = 0
  // 便利处理字典
  let result = data.map((i: any, index: number) => {
    // console.log(i.value);
    // provinDiagnose.push(i.value)
    let name = "";
  // 有 conNum 说明有子级
    if (i.conNum) {
      return {
        name: mapLocal[index],
        value: Number(i.conNum),
      };
    } else {
      if (city.find((x: any) => x === i.name)) {
        name = i.name + "市";
      } else if (area[i.name]) {
        name = area[i.name];
      } else {
        name = i.name + "省";

        // 传数据到vuex
        provinDiagnose.set(i.name,i.value);
        diagnoseCouter += Number(i.value)
      }
      return {
        name,
        value: Number(i.value),
      };
    }
  });
  // 存储数据在vuex
  home.setProvinDiagnose(provinDiagnose)
  home.setDiagnoseCouter(diagnoseCouter)


  // echarts 的数据配置选项 具体看官网
  let option = {
    title: {
      text: "中国地图",
      left: "right",
    },
    tooltip: {
      trigger: "item",
      showDelay: 0,
      transitionDuration: 0.2,
    },
    visualMap: {
      left: "right",
      min: 0,
      max: 19000,
      inRange: {
        color: [
          // "#313695",
          // "#4575b4",
          // "#74add1",
          // "#abd9e9",
          // "#e0f3f8",
          // "#ffffbf",
          // "#fee090",
          // "#fdae61",
          // "#f46d43",
          // "#d73027",
          // "#a50026",
          // "#ADFF2F",
          "#FFFFFF",
          "#ff8c71",
          '#ff5428',
          '#7f1100'

        ],
      },
      text: ["高", "低"],
      calculable: true,
    },
    series: [
      {
        name: "中国疫情地图",
        type: "map",
        roam: true,
        map: "china",
        // 设置地图的文字
        label: {
          show: true,
          fontSize: 8,
          color: "#000000",
        },
        emphasis: {
          label: {
            show: true,
          },
        },
        data: result,
      },
    ],
  };

  return option;
};

const backword = ()=>{
  location.reload();
}

</script>

<template>

  <div class="map">
    <el-button type="primary" @click="backword">返回</el-button>
    <div id="main" class="china-map" ref="mapDom"></div>
  </div>
  
</template>


<style scoped>


.map {
  /* width: 1300px;
  height: 690px; */
  /* height: 100%; */
  border: 1px solid rgb(0, 0, 0);
  border-radius: 10px;
  /* margin: 5px; */
}

.china-map{
  /* width: 1200px;
  height: 600px; */
  /* margin: auto; */
  height: 900px;
}
</style>