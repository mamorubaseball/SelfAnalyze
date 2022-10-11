<template>
  <div class="profile">
    <img :src="require('@/assets/mamoru.png')" class="profile-card-image" />
    <div class="profile-card-desc">
      <p>{{ profile.name }}</p>
      <p>{{ profile.sex }}</p>
      <p>{{ profile.old }}</p>
      <h1>残りの人生</h1>
      <h2>59年1ヶ月10日</h2>
      <h2>21280日</h2>
      <h1>今月使った時間</h1>
      <v-select
        v-model="selected"
        :items="datalist"
        label="カレンダーの種類を選択"
        outlined
      ></v-select>
      {{ profile[selected] }}h
      <!-- {{ selected }} -->
    </div>
  </div>
</template>
<script>
import { apiService } from "../../common/api.service";

export default {
  name: "profile",
  props: {},
  data() {
    return {
      profile: {},
      selected:[],
      datalist: [],
      life_women:{},
      life_men:{},

    };
  },
  methods: {
    getProfileData() {
      let endpoint = "http://127.0.0.1:8000/api/googleCalender/13";
      apiService(endpoint).then((data) => {
        this.profile = data.data;
        this.datalist = Object.keys(data.data);
      });
    },
    getLifeExpectancy(){
        let endpoint = "http://127.0.0.1:8000/api/lifeexpectancy/";
      apiService(endpoint).then((data) => {
        console.log(typeof(data.results[0].old_list_men))
      });
    }
  },
  created() {
    this.getProfileData();
    this.getLifeExpectancy()
    console.log(this.profile);
  },
};
</script>
<style>
.profile {
  box-shadow: 0 18px 200px -60px rgba(0, 0, 0, 0.981);
  border-radius: 50px; /* 角の尖り具合 */
  width: 600px;
  height: 700px;
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
