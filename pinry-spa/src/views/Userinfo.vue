<template>

  <div><PHeader></PHeader>
  <Userprofile></Userprofile>
  </div>
</template>

<script>
import PHeader from '../components/PHeader.vue';
import Userprofile from '../components/Userprofile.vue';

export default {
  name: 'Userinfo',
  data() {
  },
  components: {
    PHeader,
    Userprofile,
  },
  created() {
    this.initializeBoard();
  },
  beforeRouteUpdate(to, from, next) {
    this.filters = { userFilter: to.params.user };
    next();
  },
  methods: {
    initializeBoard() {
      this.filters = { userFilter: this.$route.params.user };
    },
  },
};
</script>
