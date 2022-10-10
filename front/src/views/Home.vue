<template>
  <div class="home">
    <profile-vue></profile-vue>
  </div>
</template>

<script>
import profileVue from '../components/profile.vue';
export default {
  name: "Home",
  components: {
    profileVue
  }
};
</script>
