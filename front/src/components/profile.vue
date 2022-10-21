<template>
  <div class="profile">
    <img :src="require('@/assets/mamoru.png')" class="profile-card-image" />
    <div class="profile-card-desc">

      <p>{{ sex }}</p>
      <p>{{ old }}</p>
      <h1>残りの人生</h1>
      <h2>59年1ヶ月10日</h2>
      <h2>21280日</h2>
      <h1>今月使った時間</h1>
      <v-select
        v-model="selectedMonth"
        :items="month"
        label="月"
        outlined
      ></v-select>

      <v-select
        v-model="selectedCalenderName"
        :items="calenderName"
        label="カレンダーの種類を選択"
        outlined
      ></v-select>

      <pie-chart></pie-chart>
      <p>{{ selectedCalenderName }}に使った時間</p>
      {{ profile[selectedMonth][selectedCalenderName]}}h
      <!-- {{ selected }} -->
    </div>
  </div>
</template>
<script>
import { apiService } from "../../common/api.service";
// import { PieChart } from './charts.vue';

export default {
  name: "profile-vue",
  components: { 
    // PieChart
  },
  props: {
    userId:String,
  },
  data() {
    return {
      profile: {},
      sex:"",
      old:0,
      selectedMonth:1,
      selectedCalenderName:"",
      month:[],
      calenderName: [],
      life_women:{},
      life_men:{},
      login:false,
    };
  },
  methods: {
    getProfileData() {
      let endpoint = "http://127.0.0.1:8000/api/user/"+this.$route.params.id;
      apiService(endpoint).then((data) => {
        this.profile = data.data[0];
        this.old = data.old;
        this.sex = data.sex;
        console.log(data.data)
        this.month = Object.keys(data.data[0]);
        this.calenderName = Object.keys(data.data[0][1]);
        
      });
    },
    getLifeExpectancy(){
        let endpoint = "http://127.0.0.1:8000/api/lifeexpectancy/";
      apiService(endpoint).then((data) => {
        console.log(data)
      });
    },
    // checkLoggedIn() {
    //   this.$session.start();
    //   if (this.$session.has("token")) {
    //       this.login = true;
    //       console.log(this.$session)
    //       console.log('login',this.login)
    //   }}
  },
  created() {
    this.getProfileData();
    this.getLifeExpectancy();
    console.log("props_id",this.$route.params.id)
  },
};
</script>
<style>
.profile {
  box-shadow: 0 18px 200px -60px rgba(0, 0, 0, 0.981);
  border-radius: 50px; /* 角の尖り具合 */
  width: 600px;
  height: 1000px;
  /* position:fixed; */
  backdrop-filter: blur(15px); /* ぼかし */
  border: 2px solid #ffffff00;
  padding: 3rem 5rem;
  flex-direction: column;
  gap: 50px;
  /* margin:  0 auto; 中央寄せ */
  margin: auto; /*中央寄せ */
  position: absolute; /* 位置指定 */
  top: 0; /* 位置指定 */
  bottom: 0; /* 位置指定 */
  left: 0; /* 位置指定 */
  right: 0;

  @media screen and (max-width: 768px;) {
    width: auto;
  }
}
.profile-card-image {
  margin: auto;
  width: 200px;
  height: 200px;
  border-radius: 50px;
  object-fit: cover;
  box-shadow: 0 20px 60px -20px rgba(13, 28, 39, -5);
}
</style>
