<template>
  <div>
    {{ getEventList }}
  </div>
</template>
<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'EventCalendar',
    created() {
      this.$store.dispatch('setEventList')
    },
    computed: {
      ...mapGetters([
        'getEventList'
      ])
    }
  }
</script>

<style></style>
