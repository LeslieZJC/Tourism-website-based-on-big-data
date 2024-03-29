<script setup lang="ts">
import { reactive } from 'vue';
import router from "@/router";
import { login } from "@/service/login";
import { useUser } from '@/stores/user';


import { ElMessage } from 'element-plus';

// pinia 
const user = useUser()

const formLabelAlign = reactive({
  email: '',
  password: ''
})

const routerActions = {
    enroll(){
      router.push({ path: '/enroll' })
    },
    home(){
      router.push({path: '/'})
    }
}
const actions = {
  loginAction(){
    login(formLabelAlign.email,formLabelAlign.password).then((res:any)=>{
        console.log(res);
       if(res.data.code===200){
         const data = res.data
          // 消息提示登录成功
          ElMessage({
            message: '登录成功，欢迎 '+data.username,
            type: 'success',
          })
          // 将token置为状态保存在pinia里面
          user.setToken(data.token)
          // 跳到首页
          routerActions.home()
          // document.cookie = "token="+data.data.token+";"
          
          console.log(data.token);
          
       }else{
         ElMessage({
          message: '用户名或者密码错误',
          type: 'error',
        })
       }
    })
  }
}


</script>

<template>
  <el-form
    label-position="left"
    label-width="80px"
    :model="formLabelAlign"
    style="max-width: 480px;"
  >
    <el-form-item label="邮箱">
      <el-input v-model="formLabelAlign.email"
        placeholder="输入邮箱"
      />
    </el-form-item>
    <el-form-item label="密码">
      <el-input
        v-model="formLabelAlign.password"
        type="password"
        placeholder="输入密码"
        show-password
         />
    </el-form-item>
  </el-form>
  <el-button type="primary" round @click="actions.loginAction">登录</el-button>
  <el-button type="success" round @click="routerActions.enroll">注册</el-button>
</template>

<style lang="scss" scoped>

</style>