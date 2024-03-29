<script setup lang="ts">

import LoginForm from "./LoginForm.vue";



</script>

<template>

    <div class="content">
            <h1>大数据下的红色景点推荐系统</h1>
            <div class="main-content">
                <div style="width: auto;">
                    <label class="font">登录界面</label>
                </div>
                <div style="width: auto;">
                    <LoginForm></LoginForm>
                </div>
                <!-- <div style="margin: 0 auto;">

                </div>    -->
            </div>
           
    </div>




</template>

<style scoped>


.content{
    width: 50%;
    height: 50%;
    border: 1px solid var(--el-border-color);
    border-radius: 1%;
 

    margin: 0 auto;
       margin-top: 10px;
    /* margin-top: 5%; */
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

.main-content{
    width: 60%;
    margin-bottom: 20%;
    /* margin: 0 0; */
    margin-top: 5%;
    position: relative;
    top: 50px;
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