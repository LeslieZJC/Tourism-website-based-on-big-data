<script setup lang="ts">
import LabelDialogVue from './LabelDialog.vue';
import HomeView from './HomeView.vue';
import Head from './Head.vue';
import Recommon from './Recommon.vue';
import ReView from './ReView.vue';


</script>

<template>
      <LabelDialogVue></LabelDialogVue>


<div class="home">
    <div class="top-bar">
         <Head></Head>
    </div>

    <div class="main-content">
        <div class="left-content">
            <ReView></ReView>
        </div>

        <div class="center-content">
            <HomeView></HomeView>
        </div>

        <div class="right-content">
            <Recommon></Recommon>
        </div>
    </div>

</div>

      
</template>

<style scoped>
    .home {
        display: flex;
        flex-direction: column;
        height: 100%;
    }


    .top-bar {
        flex: 3;
        /* background-color: rebeccapurple; */
    }

    .main-content {
        flex: 8;
        /* background-color: aqua; */

        display: flex;
    }

    .left-content {
        flex: 1;
        /* background-color: black; */
    }

    .center-content {
        flex: 4;
        /* background-color: aliceblue; */
    }

    .right-content {
        flex: 2;
        /* background-color: blue; */
    }
</style>