import Vue from 'vue'
import Vuex from 'Vuex'
import client from "@/api"
import router from "@/router"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    eventList: [],
  },
  mutations: {
    setEventList(state, res){
      state.eventList = res
    }
  },
  actions: {
    setEventList({commit}){
      return client.main.eventList().then(res => {
        commit('setEventList', res.data)
      })
    }
  },
  getters: {
    getEventList(state){
      return state.eventList
    }
  }
})
