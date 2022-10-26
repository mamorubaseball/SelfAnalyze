<template>
  <div class="home">
    <!-- <barcharts :chart-data="data" :options="options"></barcharts> -->
    <profile-vue></profile-vue>
  </div>
</template>

<script>
import profileVue from '@/components/Profile.vue';
// import Barcharts from '@/components/Barcharts.vue';


export default {

  name: "Home",
  components: {
    profileVue,
    // Barcharts,
},
};
</script>
