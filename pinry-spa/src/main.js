import Buefy from 'buefy';
import Vue from 'vue';
import { VueMasonryPlugin } from 'vue-masonry';
import VueI18n from 'vue-i18n';
import App from './App.vue';
import router from './router';
import setUpAxiosCsrfConfig from './components/utils/csrf';
import './registerServiceWorker';

Vue.config.productionTip = false;
Vue.use(Buefy);
Vue.use(VueMasonryPlugin);
Vue.use(VueI18n);
setUpAxiosCsrfConfig();

function getBrouserLang(defaultValue) {
  const langClip = navigator.language.substr(0, 2); // 获取浏览器配置语言前两位;

  if (langClip !== '') {
    return langClip;
  }
  return defaultValue;
}

const i18n = new VueI18n({
  // locale: 'en_US',
  locale: getBrouserLang('zh'), // 语言标识 默认中文
  messages: {
    zh: require('./assets/lang/zh'), // 中文语言包
    en: require('./assets/lang/en'), // 英文语言包
    ja: require('./assets/lang/ja'), // 英文语言包
  },
});

new Vue({
  router,
  i18n,
  render: h => h(App),
}).$mount('#app');
