import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import profileVue from '../src/components/profile.vue';
Vue.config.productionTip = false;


new Vue({
  router,
  store,
  vuetify,
  components:{'profile-vue':profileVue},
  render: h => h(App)
}).$mount("#app");
