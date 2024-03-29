<script setup lang="ts">
import enrollForm from "./enrollForm.vue";
import router from "@/router";

const routerActions = {
    back(){
        router.push({ path: '/login' })
    }
}

</script>

<template>

    <div class="content">
        <!-- <div class="form"> -->
            <div class="main">
                <div style="width: auto;">
                    <label class="font">注册界面</label>
                </div>
                <div style="width: auto;">
                    <enrollForm></enrollForm>
                </div>
                <div >
                    <el-button type="primary" round>确定</el-button>
                    <el-button type="warning" round @click="routerActions.back">返回</el-button>
                </div>   
            </div>
           
    </div>




</template>

<style scoped>


.content{
    width: 50%;
    height: 50%;
    border: 1px solid var(--el-border-color);
    border-radius: 1%;
    margin-top: 20px;

    margin: 0 auto;
    margin-top: 10%;
    background-color: rgb(255, 255, 255);
    display: flex;
    justify-content: center;
    align-items: center;
    /* justify-content: space-between; */
    flex-wrap: wrap;

}
.form{
    /* width: 50%; */
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;

}

.main{
    width: 60%;
    margin: 0 auto;
}

.font{
/* margin:0px;  */
/* margin-left: 20%; */
font-weight: 600;
font-size: 28px;
font-family: "黑体";
color: #8c888b;
background: -webkit-linear-gradient(45deg, #70f7fe, #fbd7c6, #fdefac, #bfb5dd, #bed5f5);

color: transparent;

-webkit-background-clip: text;

animation: ran 10s linear infinite;
}

</style>