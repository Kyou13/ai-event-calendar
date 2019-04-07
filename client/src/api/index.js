import axios from 'axios'
import main from './main'

const client = axios.create({
  baseURL: "http://localhost:8000/",
})

client.main = main(client)

client.install = function (Vue) {
  Object.defineProperty(Vue.prototype, '$request', {
    get () {
      return client
    },
  })
}

export default client
