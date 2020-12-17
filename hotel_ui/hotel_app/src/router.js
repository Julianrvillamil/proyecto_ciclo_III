import vueRouter from 'vue-router'

import User from './components/User'
import UserCount from './components/UserCount'//UserBalance
import App from './App'

const router = new vueRouter({
    mode: 'history',
    base: __dirname,
    routes: [
        {
        path: '/',
        name: "root",
        component: App
        },
        {
        path: '/user/:username',
        name: "user",
        component: User
        },
        {
        path: '/user/count/:username',
        name: "user_count",
        component: UserCount
        },
    ]
})
export default router