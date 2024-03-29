<script setup lang="ts">
const props = defineProps({
    avater:String,
    title:String,
    introduce:String,
    id:Number
})
const path = "/details?attractionId="+String(props.id)



</script>

<template>
        <router-link :to="`/details?attractionId=`+String(props.id)" class="attraction">
            <el-avatar    :size="50" :src="avater" class="avatar"/>
            <div style="display: block;">
                <div ><a href="">{{title}}</a></div>
                <div class="introduce"><a href="">{{introduce}}</a></div>
            </div>

        </router-link>
</template>

<style scoped>

a {
    text-decoration: none;
    color: rgb(10, 9, 9);
}

.attraction {
    display: flex;
    flex-wrap: nowrap;
    margin-bottom: 10px;
}

.introduce {
    width: 340px;
    height: 20px;
    overflow: hidden;
    text-overflow: ellipsis; 
}

.avatar {
    height: 50px;
    width: 50px;
    margin-right: 10px;
}




</style>