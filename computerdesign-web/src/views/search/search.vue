<script setup lang="ts">
import { useRoute } from 'vue-router';
import List from './list.vue';
import Head from '../home/Head.vue';


</script>

<template>
    <div class="search">
        <div class="top-bar">
            <Head></Head>
        </div>

        <div class="attractions-list">
            <List></List>
        </div>
    </div>
</template>

<style scoped>
.search {
    height: 100%
}

.top-bar {
    height: 70px;
}


.attractions-list {
    background-color: rgb(238, 238, 238);
    height: 850px;
    width: 60%;
    margin: 0 auto;
}

</style>