<template>
  <div class="profile">
    <img :src="account_image_src" class="profile-card-image" />
    <div class="profile-card-desc">
      <h1>残りの人生</h1>
      <h2>59年1ヶ月10日</h2>
      <h2>21280日</h2>
      <h1>今月使った時間</h1>
      <v-select
        v-model="selectedMonth"
        :items="month"
        label="月"
        outlined
        @change="ChangeCalenderData"
      ></v-select>
      <!-- <p>{{ selectedCalenderName }}に使った時間</p>
      {{ profile[selectedMonth][selectedCalenderName]}}h -->
      <div v-if="isShow">
            <v-row align="center" justify="center" class="ma-1">
              <v-btn-toggle v-model="toggle_exclusive" mandatory>
                <v-btn>
                  <v-icon>mdi-chart-bar</v-icon>
                </v-btn>
                <v-btn>
                  <v-icon>mdi-chart-bar</v-icon>
                </v-btn>
              </v-btn-toggle>
            </v-row>
        <div v-if="toggle_exclusive">
          <bar-chart :chart-data="data" :options="options" justify="center"></bar-chart>
        </div>
        <div v-else>
          <pie-chart :chart-data="data" :options="options"></pie-chart>
        </div>

      </div>
    </div>
  </div>
</template>
<script>
import { apiService } from "../../common/api.service";
import BarChart from "./Barchart.vue";
import PieChart from "./Piechart.vue";

export default {
  name: "profile-vue",
  components: {
    BarChart,
    PieChart,
  },
  props: {
    userId: String,
  },
  data() {
    return {
      profile: {},
      sex: "",
      old: 0,
      account_image_src: "",
      selectedMonth: 1,
      selectedCalenderName: "",
      month: [],
      calenderName: [],
      calenderNumber: 0,
      life_women: {},
      life_men: {},
      login: false,
      isShow: false,
      toggle_exclusive: undefined,
      data: {
        labels: [],
        datasets: [
          {
            label: "グラフ",
            data: [],
            backgroundColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
              "rgba(255, 159, 30, 1)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 0.2)",
              "rgba(255, 159, 30, 0.3)",
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        legend:{
          display:true //グラフに表示される凡例を削除できます。
        }
      },
    };
  },
  methods: {
    getProfileData() {
      let endpoint = "http://127.0.0.1:8000/api/user/" + this.$route.params.id;
      apiService(endpoint).then((data) => {
        this.profile = data.data[0];
        this.old = data.old;
        this.sex = data.sex;
        this.account_image_src = data.account_image;
        this.month = Object.keys(data.data[0]);
        this.calenderName = Object.keys(data.data[0][1]);
        this.calenderNumber = this.calenderName.length;
      });
    },
    getLifeExpectancy() {
      let endpoint = "http://127.0.0.1:8000/api/lifeexpectancy/";
      apiService(endpoint).then((data) => {
        console.log(data);
      });
    },
    ChangeCalenderData(month) {
      this.data.labels = [];
      this.data.datasets[0].data = [];
      for (var i = 0; i < this.calenderNumber; i++) {
        console.log(i);
        var calender_label = Object.keys(this.profile[month])[i];
        var calender_data = Object.values(this.profile[month])[i];
        if (calender_data != 0) {
          this.data.labels.push(calender_label);
          this.data.datasets[0].data.push(calender_data);
        }
      }
      this.isShow = true;
    },
  },
  created() {
    this.getProfileData();
    this.getLifeExpectancy();
  },
  mounted() {
    // this.data.labels = this.profile[1]
    console.log(this.toggle_exclusive)
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
