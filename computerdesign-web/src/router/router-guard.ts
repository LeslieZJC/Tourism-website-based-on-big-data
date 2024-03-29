import { useUser } from '@/stores/user'
import type { Router } from 'vue-router'

export default function registerRouterGuard(router: Router): void {
  //前置路由导航配置
  router.beforeEach((to, from,next) => {
    const user = useUser()
    
    if (to.path!='/login' &&  user.token ==="") {
      // 设置标签名
      document.title = String(to.meta.title) 
      next({ path: '/login' });
    }else{
      document.title = String(to.meta.title) 
      next();
    }
    
  })
}
