<script setup lang="ts">
import { reactive } from 'vue';

const formLabelAlign = reactive({
  email: '',
  password: '',
  username:''
})
</script>

<template>
  <el-form
    label-position="left"
    label-width="80px"
    :model="formLabelAlign"
    style="max-width: 480px;"
  >

    <el-form-item label="用户名">
      <el-input v-model="formLabelAlign.username"
        placeholder="输入用户名"
      />
    </el-form-item>
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
</template>

<style lang="scss" scoped>

</style>