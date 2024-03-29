<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
// import HelloWorld from '@/components/HelloWorld.vue'
</script>

<template>
  <!-- <div class="wrapper">
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </nav>
  </div> -->

  <RouterView />  


</template>

<style>
html,body {
  height: 100%;

}

* {
    margin: 0;
    padding: 0;
    list-style: none;
    font-family: Helvetica, 'Hiragino Sans GB', 'Microsoft Yahei', '微软雅黑', Arial, sans-serif;
}


#app {
  height: 100%;
  width: 100%;
  /* margin: 0 auto; */
  /* font-weight: normal; */
  /* background: url("@/assets/images/login-bg.svg"); */
  /* background: url("@/assets/images/pexels-fwstudio-129731.jpg"); */
  background-color: rgb(255, 255, 255);
  
}


</style>
