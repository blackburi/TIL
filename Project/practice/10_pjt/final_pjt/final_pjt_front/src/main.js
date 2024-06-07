import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue'
import router from './router'

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import "@/assets/styles/main.css"
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import {
  faSearch,
  faStar as fasStar,
  faCommentDots,
  faHome,
  faPhone,
  faUser,
  faChevronRight,
  faBuilding,
  faMapMarkedAlt,
  faMapMarker,
  faEnvelope,
  faSpinner,
  faUnlock,
  faUserShield,
  faSignOutAlt,
  faUserCircle,
  faUserEdit,
  faEraser,
  faAngleLeft,
  faPaperclip,
  faKey,
  faImage,
  faUpload,
  faSchool,
  faInfoCircle,
  faSignInAlt,
  faUserPlus,
  faSignature,
  faTable,
  faThumbsUp,
  faShare,
  faComment,
} from '@fortawesome/free-solid-svg-icons'
import { faStar as farStar } from '@fortawesome/free-regular-svg-icons'
import { faThumbsUp as farThumbsUp } from '@fortawesome/free-regular-svg-icons'

library.add(
  faSearch,
  fasStar,
  farStar,
  faCommentDots,
  faHome,
  faPhone,
  faUser,
  faChevronRight,
  faBuilding,
  faMapMarkedAlt,
  faMapMarker,
  faEnvelope,
  faSpinner,
  faUnlock,
  faUserShield,
  faSignOutAlt,
  faUserCircle,
  faUserEdit,
  faEraser,
  faAngleLeft,
  faPaperclip,
  faKey,
  faImage,
  faUpload,
  faSchool,
  faInfoCircle,
  faSignInAlt,
  faUserPlus,
  faSignature,
  faTable,
  faThumbsUp,
  faShare,
  farThumbsUp,
  faComment,
)

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

app.use(pinia)
app.use(router)

app.mount('#app')
