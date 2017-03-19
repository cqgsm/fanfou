import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import Login from '@/views/login/Login'

Vue.use(Router)

const routes = [{
    path: '/',
    name: 'Hello',
    component: Hello
},{
    path: '/login',
    name: 'Login',
    component: Login
}]

const router = new Router({
    routes
})

// 路由全局钩子
/**
 * to: Route: 即将要进入的目标 路由对象
 * from: Route: 当前导航正要离开的路由
 * ？？  meta: { requiresAuth: true }
 * token 过期还要跳转到登陆页面 ？ 先不管过期
 */
router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        // 有token 说明登陆了
        if (store.state.token) {
            next();
        } else {
            next({
                path: '/login',
                query: {
                    redirect: to.fullPath
                }
            })
        }
    } else {
        next();
    }
})

export default router;
