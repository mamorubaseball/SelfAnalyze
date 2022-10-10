<template>
  <div>
    <v-container>
      <h1>USER Information</h1>
      <input type="text" v-model="email" />
      <p>userアドレス:{{ email }}</p>

      <!-- <v-bth @click="getUserInfo">ゲット</v-bth> -->
      <!-- <p> {{user.results[0].name}}</p> -->
      <!-- <p> {{user.results[0].email}}</p> -->
      <!-- <p> {{user.results[0].data}}</p> -->
    </v-container>
  </div>
</template>

<script>
import { apiService } from "/Users/mamoru/アプリケーション(web)/SelfAnalyze/front/common/api.service.js";

export default {
  name: "user",
  data() {
    return {
      email: "",
      user: {}
    };
  },
  methods: {
    // 詳細画面に遷移したらデータをjob変数に格納して、画面のタイトルを会社名に変更している。
    getUserInfo() {
      let endpoint = "http://127.0.0.1:8000/api/googleCalender/";
      console.log(endpoint);
      apiService(endpoint).then(data => {
        this.user = data;
        // this.setPageTitle(data.company_name);
      });
    }
  },
  created() {
    this.getUserInfo();
  }
};
</script>
