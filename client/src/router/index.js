import Vue from 'vue'
import Router from 'vue-router'
import EventCalendar from '@/views/EventCalendar'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'EventCalendar',
      component: EventCalendar
    }
  ]
})
