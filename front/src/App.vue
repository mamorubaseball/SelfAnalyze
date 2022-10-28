<template>
  <v-app>
    <v-app-bar 
    app 
    dark
    elevation="12"
    
    src="@/assets/profile_bg.png" 
    hide-on-scroll>
    
      <v-toolbar-title>自己分析ツール</v-toolbar-title>
      <v-spacer></v-spacer>
      <div>
        <v-btn color="green" class="ma-2"  to="/login"><v-icon>mdi-login-variant</v-icon>ログイン</v-btn>
        <v-btn color="green" class="ma-2"  to="/"><v-icon>mdi-logout-variant</v-icon>ログアウト</v-btn>
      </div>
    </v-app-bar>
    <v-main>

    <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  })
};
</script>

<style>
  #app {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    height: 1500px;
  /* 背景 */
    background-image: url("assets/profile_bg.png");
    background-size: cover;
  }
  #nav {
    padding: 30px;
  }

  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }

  #nav a.router-link-exact-active {
    color: #42b983;
  }

  .bar{
    background-color: #6519c8;
  }
</style> 