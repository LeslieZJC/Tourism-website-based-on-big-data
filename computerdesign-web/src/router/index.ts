import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/home/Home.vue'

import registerRouterGuard from './router-guard'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta:{
        title:'首页-欢迎登录'
      }
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/login',
      name: 'login',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/login/Login.vue'),
      meta:{
        title:'疫情下红色景点推荐-登录'
      }
    },
    {
      path: '/enroll',
      name: 'enroll',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/enroll/enroll.vue'),
      meta:{
        title:'注册'
      }
    },
    {
      path: '/search',
      name: 'search',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/search/search.vue'),
      meta:{
        title:'搜索结果'
      }
    },
    {
      path: '/details',
      name: 'details',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/details/index.vue'),
      meta:{
        title:'景点详情'
      }
    }

  ]
})

registerRouterGuard(router)

export default router
