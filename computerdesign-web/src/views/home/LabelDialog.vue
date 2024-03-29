<script setup lang="ts">
import { useHome } from '@/stores/home';
// import { computed } from '@vue/reactivity';
import { ref, computed } from 'vue'
import { ElMessage } from 'element-plus'
import { getRealRecommon } from '@/service/home';
interface Tag{
    name:string,
    type:string
}

const myTags = ref([] as Tag[])


const tags = ref([
    { name: '北京', type: '' },
    { name: '上海', type: 'success' },
    { name: '天津', type: 'info' },
    { name: '重庆', type: 'warning' },
    { name: '黑龙江', type: '' },
    { name: '辽宁', type: 'danger' },
    { name: '吉林', type: 'info' },
    { name: '河北', type: 'danger' },
    { name: '河南', type: 'danger' },
    { name: '湖北', type: 'success' },
    { name: '湖南', type: 'danger' },
        { name: '山东', type: 'danger' },
    { name: '山西', type: 'danger' },
    { name: '陕西', type: 'success' },
    { name: '安徽', type: 'danger' },
        { name: '浙江', type: 'danger' },
    { name: '江苏', type: 'danger' },
    { name: '福建', type: 'success' },
    { name: '广东', type: 'danger' },
        { name: '海南', type: 'danger' },
    { name: '四川', type: 'success' },
    { name: '云南', type: 'danger' },
        { name: '贵州', type: 'danger' },
    { name: '青海', type: 'success' },
    { name: '甘肃', type: 'danger' },
        { name: '江西', type: 'danger' },
    { name: '台湾', type: 'success' }
])
const tagsType1 = ref([
  { name: '人文景观', type: 'warning' },
  { name: '现代文明', type: 'success' },
  { name: '自然风光', type: '' }
])
const tagsType2 = ref([
  { name: '拍照', type: 'warning' },
  { name: '好汉', type: 'success' },
  { name: '建筑', type: 'info' },
  { name: '巡山', type: '' },
  { name: '北京', type: 'success' },
  { name: '体验', type: 'warning' },
  { name: '性价比', type: '' },
  { name: '姹紫嫣红', type: '' },
  { name: '孩子', type: 'info' },
    { name: '年票', type: 'warning' },
  { name: '亲王', type: 'success' },
  { name: '拍照', type: 'info' },
  { name: '刺激', type: '' },
  { name: '表演', type: 'success' },
  { name: '野生动物', type: 'warning' },
  { name: '浦江', type: '' },
  { name: '疫情', type: '' },
  { name: '自然科', type: 'info' },
    { name: '宝山', type: 'warning' },
  { name: '商业', type: 'success' }
])



const actions = {
    handleClose(name: string,type: string){
        for(let i in tags.value){
            // console.log(i);

            if(myTags.value[Number(i)].name == name){
                myTags.value.splice(Number(i), 1)
                break
            }
            
        }
    },
    handleClick(name:string,type:string){
        // console.log("点击了");
        myTags.value.push({name,type})
        // console.log(myTags);
        
    }
}

// 是否可视化
const home = useHome()
const dialogVisible = computed(()=>home.$state.labelVisable)

// 获取省份，类别和标签
const provinces = ref("")
const category = ref("")
const selecttags = ref<string[]>([])

const dialogActions = {
    upDateUserLabel(){
        if(myTags.value.length>=8){
            // 同时发送axios请求，获取后端推荐的数据
            provinces.value = myTags.value[0].name
            category.value = myTags.value[1].name
            for(let i=2;i<myTags.value.length;i++){
                selecttags.value?.push(myTags.value[i].name)
            }
            getRealRecommon(provinces.value,category.value,selecttags.value).then((res)=>{
                // console.log("准确推荐的景点",res.data);
                home.setRecommonsAttraction(res.data.Recommd)
            })

            // 不在显示这个对话框
            home.setLabelVisablen(false)
            ElMessage({
                message: '选择标签成功',
                type: 'success',
            })
        }else{
            ElMessage({
                message: '请选择八个标签',
                type: 'error',
            })
        }


    }
}

</script>

<template>
    <div >
        <el-dialog v-model="dialogVisible" title="选择旅游偏好" width="40%" draggable >
            <div >
                <div class="my-label">我选择的标签: </div>
                <br>
                <div class="labelList">
                    <div v-for="tag in myTags" :key="tag.name">
                        <el-space alignment="start" :size="10" direction="vertical">
                        <el-space alignment="start" :size="10">
                            <el-tag
                                class="mx-1 el-tag"
                                closable
                                :type="tag.type"
                                @close="actions.handleClose(tag.name,tag.type)"
                            >
                                {{ tag.name }}
                            </el-tag>
                        </el-space>
                        </el-space>
                    </div>
                </div>
            </div>

            <div>
                <label class="my-label">省份: </label>
                <br>
                <div class="labelList">
                    <div  v-for="tag in tags" :key="tag.name">
                        <el-space alignment="start" :size="10">
                        <el-tag
                            class="mx-1 el-tag"
                            :type="tag.type"
                            @click="actions.handleClick(tag.name,tag.type)"
                        >
                            {{ tag.name }}
                        </el-tag>
                        </el-space>
                    </div>
                </div>
                <br>
                <label class="my-label">景点类型: </label>
                <br>
                <div class="labelList">
                    <div  v-for="tag in tagsType1" :key="tag.name">
                        <el-space alignment="start" :size="10">
                        <el-tag
                            class="mx-1 el-tag"
                            :type="tag.type"
                            @click="actions.handleClick(tag.name,tag.type)"
                        >
                            {{ tag.name }}
                        </el-tag>
                        </el-space>
                    </div>
                </div>
                <br>
                <label class="my-label">景点主题: </label>
                <br>
                <div class="labelList">
                    <div  v-for="tag in tagsType2" :key="tag.name">
                        <el-space alignment="start" :size="10">
                        <el-tag
                            class="mx-1 el-tag"
                            :type="tag.type"
                            @click="actions.handleClick(tag.name,tag.type)"
                        >
                            {{ tag.name }}
                        </el-tag>
                        </el-space>
                    </div>
                </div>
                    
            </div>

            <template #footer>
            <span class="dialog-footer">
                <el-button @click="dialogActions.upDateUserLabel">取消</el-button>
                <el-button type="primary" @click="dialogActions.upDateUserLabel"
                >确定</el-button
                >
            </span>
            </template>
        </el-dialog>
    </div>
</template>

<style scoped>

.el-tag:hover{
    cursor: pointer;
}


.labelList{
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    /* overflow: auto; */
}

.my-label{
    display: flex;
    flex-wrap: wrap;
    
    font-family: KaiTi;
    font-weight: 600;

}

</style>