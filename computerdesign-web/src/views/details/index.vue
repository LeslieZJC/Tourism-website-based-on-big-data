<script setup lang="ts">
import type { Attract } from '@/service/home/type';
import { ref, computed, watch } from 'vue';
import { useRoute } from 'vue-router';
import Head from '../home/Head.vue';

import { getComment, getDetails, getLable, addCollect, disCollect } from '@/service/details';
import { getCollection } from '@/service/home';
import { ElMessage } from 'element-plus'
import AttRecommd from './AttRecommd.vue'

// 获取路由传递的参数并且发axios请求
const route = useRoute()
const attractionId = ref(route.query.attractionId)
// console.log(attractionId);
// 请求到的景点
const attraction = ref<Attract>()
// 是否为高风险地区
const badge = ref("")
const badgetype = ref("")






// 评论分页
const currentPage = ref(1)
const pageSize = ref()
const total = ref()
const small = ref(false)
const background = ref(true)

const activeName = ref('info')
const handleSizeChange = (val: number) => {

}
const handleCurrentChange = (val: number) => {
    // 点击分页重新发送axios请求
    getComment(Number(attractionId.value), Number(currentPage.value)).then((res) => {
        // console.log(res.data);
        const data = res.data
        if (data.code == 200) {
            comments.value = data.PageUtils.list
            total.value = data.PageUtils.totalCount
            pageSize.value = data.PageUtils.pageSize
        }

    })
}

// 请求当前景点的评论
// 定义评论
const comments = ref<string[]>([])



//请求标签
const lables = ref<{
    provinces: string,
    sort: string,
    theme1: string,
    theme2: string,

    theme3: string,
    theme4: string,
    theme5: string,
    theme6: string,
}>()



// 请求用户收藏的景点
// const ids = ref([-1])
const flag = ref(false)



const collection = () => {
    flag.value = true;

    addCollect(Number(attractionId.value))

    ElMessage({
        message: '收藏成功.',
        type: 'success',
    })
}
const disCollection = () => {
    flag.value = false;
    disCollect(Number(attractionId.value))

    ElMessage({
        message: '取消收藏.',
        type: 'success',
    })
}



function getData() {

    getLable(Number(attractionId.value)).then((res) => {
    const data = res.data
    if (data.code === 200) {
        lables.value = data.lable
        // console.log(lables.value);

    }
})
    getDetails(Number(attractionId.value)).then((res) => {
        // console.log(res.data);
        attraction.value = res.data.details


        // console.log(attraction.value);

        if (attraction.value?.risks == 1) {
            badge.value = "高风险";
            badgetype.value = "danger"
        } else {
            badge.value = "安全";
            badgetype.value = "success"
        }


    })

    getComment(Number(attractionId.value), Number(currentPage.value)).then((res) => {
        // console.log(res.data);
        // attraction.value = res.data.details
        const data = res.data
        if (data.code == 200) {
            comments.value = data.PageUtils.list
            // console.log(comments.value);
            total.value = data.PageUtils.totalCount
            pageSize.value = data.PageUtils.pageSize
        }

    })

    getCollection().then((res: any) => {
        //   console.log(res.data);
        const data = res.data
        if (data.code == 200) {
            // console.log(data);
            for (let i = 0; i < data.collection.length; i++) {
                // ids.value.push(data.collection[i].id) 
                if (Number(attractionId.value) === Number(data.collection[i].id)) {
                    flag.value = true
                    break
                }
            }
            console.log("flag", flag.value);

        }

    })
}

getData()

watch(() => route.query.attractionId, (newValue, oldValue) => {
    attractionId.value = newValue
    getData()
    
})


</script>

<template>
    <div class="details">
        <div class="top-bar">

            <Head></Head>
        </div>

        <div class="attractions-list">
            <!-- 标题 -->
            <div class="title">
                <div>
                    {{ attraction?.title }}
                    <el-tag :type="badgetype">
                        {{ badge }}
                    </el-tag>
                </div>
                <div v-if="flag" style="display: flex; flex-wrap: nowrap;align-items: center;left: 60%;">
                    <el-icon :size="35">
                        <star-filled />
                    </el-icon>
                    <div style="color: rgb(77, 73, 73);">

                        <el-button type="text" size="large" @click="disCollection">已收藏</el-button>
                    </div>
                </div>

                <div v-else style="display: flex; flex-wrap: nowrap;align-items: center;left: 60%;">
                    <el-icon :size="30">
                        <star />
                    </el-icon>
                    <div style="color: rgb(77, 73, 73);">
                        <el-button type="text" size="large" @click="collection">收藏</el-button>
                    </div>
                </div>

            </div>
            <!-- 面包屑 -->
            <div style="margin-left: 40px;margin-top: 5px;">
                <el-breadcrumb separator="/">
                    <el-breadcrumb-item>{{ lables?.provinces }}</el-breadcrumb-item>
                    <el-breadcrumb-item>{{ lables?.sort }}</el-breadcrumb-item>

                    <el-breadcrumb-item>{{ lables?.theme1 }}</el-breadcrumb-item>
                    <el-breadcrumb-item>{{ lables?.theme2 }}</el-breadcrumb-item>
                    <el-breadcrumb-item>{{ lables?.theme3 }}</el-breadcrumb-item>

                    <el-breadcrumb-item>{{ lables?.theme4 }}</el-breadcrumb-item>
                    <el-breadcrumb-item>{{ lables?.theme5 }}</el-breadcrumb-item>

                    <el-breadcrumb-item>{{ lables?.theme6 }}</el-breadcrumb-item>
                </el-breadcrumb>
            </div>
            <el-divider border-style="double" />

            <div class="demo-image__lazy">
                <el-image :src="attraction?.avate" lazy />
            </div>

            <el-divider border-style="double" />
            <div>
                <el-tabs v-model="activeName" type="card" class="demo-tabs">
                    <el-tab-pane label="介绍" name="info">
                        <div class="info">
                            {{ attraction?.info }}
                        </div>
                    </el-tab-pane>
                </el-tabs>
            </div>

            <el-divider border-style="double" />

            <div>
                <el-tabs v-model="activeName" type="card" class="demo-tabs">
                    <el-tab-pane label="评论" name="info">
                        <div class="comments">
                            <el-card class="box-card">
                                <div v-for="(comment, index) in comments" :key="index" class="text item">
                                    {{ comment }}
                                    <el-divider border-style="double" />
                                </div>
                            </el-card>

                            <div class="footer">
                                <div class="pagination-block">
                                    <el-pagination v-model:currentPage="currentPage" v-model:page-size="pageSize"
                                        :small="small" :background="background" layout="prev, pager, next, jumper"
                                        :total="total" @size-change="handleSizeChange"
                                        @current-change="handleCurrentChange" />
                                </div>
                            </div>
                        </div>
                    </el-tab-pane>
                </el-tabs>
            </div>

            <AttRecommd :attractionId="Number(attractionId)"></AttRecommd>



        </div>
    </div>
</template>

<style scoped>
.details {
    height: 100%
}

.top-bar {
    height: 70px;
    /* background-color: aqua; */
}


.attractions-list {
    background-color: rgb(255, 255, 255);

    /* height: 850px; */
    height: 100%;
    width: 60%;
    margin: 0 auto;
}

.attractions-list>div {
    margin-top: 10px;
    margin-bottom: 10px;
}


.title {
    display: flex;
    flex-wrap: nowrap;
    /* margin-top: 10px; */
}

.title>div:nth-child(1) {
    margin-left: 40px;
    font-family: "Arial", "Microsoft YaHei", "黑体", "宋体", sans-serif;
    font-size: 35px;
    font-weight: 500;
}

.title>div:nth-child(2) {
    position: relative;
    left: 60%;
    font-size: 20px;
    font-weight: 500;

}

/* .title>div:nth-child(3) {
    position: relative;
    left: 70%;
    font-size: 20px;
    font-weight: 500;
    
} */

.info {
    text-indent: 2em;
    font-family: Helvetica, 'Hiragino Sans GB', 'Microsoft Yahei', '微软雅黑', Arial, sans-serif;
    color: rgb(83, 79, 79);
}

.comments {
    margin-top: 5px;
}

.recommd {
    margin-top: 5px;
}


.demo-image__lazy {
    height: 450px;
    width: 90%;
    margin: 0 auto;
    overflow-y: auto;
}

.demo-image__lazy .el-image {
    display: block;
    min-height: 200px;
    margin-bottom: 10px;
}

.demo-image__lazy .el-image:last-child {
    margin-bottom: 0;
}

.time {
    font-size: 12px;
    color: #999;
}

.bottom {
    margin-top: 13px;
    line-height: 12px;
    display: flex;
    flex-wrap: nowrap;
    /* justify-content: space-between;
  align-items: center; */
}

.image {
    width: 100%;
    display: block;
}

.card-image {
    display: flex;
    flex-wrap: nowrap;
    /* justify-content: space-around; */
    /* margin-left: 5px; */

}

img {
    /* padding: 10px; */
}


.footer {
    margin-top: 5px;

    display: flex;
    justify-content: center;
}



/* .img-card:nth-child(1) {
    flex: 1;
    background-color: azure;

}
.img-card:nth-child(2) {
    flex: 1;
    background-color: black;

}
.img-card:nth-child(3) {
    flex: 1;
    background-color: blue;

} */
</style>