import './style.css'
import { Router } from 'vue-router'
import App from './App.vue'
import router from './router/index.js'
// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { createApp } from 'vue'


createApp(App).use(router).mount('#app')
