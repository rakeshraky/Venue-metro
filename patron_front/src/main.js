import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'
import * as VueGoogleMaps from 'vue2-google-maps'
import VueGeolocation from 'vue-browser-geolocation'
import Paginate from 'vuejs-paginate'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faUserSecret)

Vue.component('font-awesome-icon', FontAwesomeIcon)


Vue.component('VueSlider', VueSlider)
Vue.component('paginate', Paginate)


Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(VueGeolocation)

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyCo2auxZ6qQW251NxKoXX_bH6o5ptnmELY',
    libraries: ['places', 'geometry'],
  },
 
  //// If you intend to programmatically custom event listener code
  //// (e.g. `this.$refs.gmap.$on('zoom_changed', someFunc)`)
  //// instead of going through Vue templates (e.g. `<GmapMap @zoom_changed="someFunc">`)
  //// you might need to turn this on.
  // autobindAllEvents: false,
 
  //// If you want to manually install components, e.g.
  //// import {GmapMarker} from 'vue2-google-maps/src/components/marker'
  //// Vue.component('GmapMarker', GmapMarker)
  //// then disable the following:
  installComponents: true,
})

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'



new Vue({
  render: h => h(App)
}).$mount('#app')
