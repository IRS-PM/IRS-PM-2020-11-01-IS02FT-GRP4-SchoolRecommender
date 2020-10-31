import Vue from 'vue'
import VueRouter from 'vue-router'
import routes from './router/router'
import ajax from './config/ajax'
import './style/common'
import './config/rem'
import ElementUI from 'element-ui' //element-ui的全部组件
import 'element-ui/lib/theme-chalk/index.css'//element-ui的css
Vue.use(ElementUI) //使用elementUI
Vue.use(VueRouter)
const router = new VueRouter({
	routes
})

new Vue({
	router,
}).$mount('#app')

