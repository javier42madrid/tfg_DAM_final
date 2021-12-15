import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/home/home.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/login/login.vue')
    },
    {
      path: '/user',
      name: 'user',
      component: () => import('@/views/user/user.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('@/views/register/register.vue')
    },
    {
      path: '/forgot_password',
      name: 'forgot_password',
      component: () => import('@/views/forgot_password/forgot_password.vue')
    },
    {
      path: '/default_user',
      name: 'default_user',
      component: () => import('@/views/default_user/default_user.vue')
    }
  ]
})
