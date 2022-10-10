<template>
  <div class="about">
    <h1>This is an about page</h1>
    <v-container grid-list-md>
      <v-layout row wrap align-center justify-center fill-height>
        <v-flex xs12 sm8 lg4 md5>
          <v-card class="login-card">
            <v-card-title>
              <span class="headline">Login to HedgeHogs</span>
            </v-card-title>

            <v-spacer />

            <v-card-text>
              <v-form ref="form" v-model="valid" lazy-validation>
                <v-container>
                  <v-text-field
                    v-model="credentials"
                    :counter="70"
                    label="Eメールアドレス"
                    maxlength="70"
                    required
                  />

                  <v-text-field
                    type="password"
                    v-model="credentials"
                    :counter="20"
                    label="パスワード"
                    maxlength="20"
                    required
                  />
                </v-container>
                <v-btn class="pink white--text" @click="login">Login</v-btn>
              </v-form>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "About",
  data: () => ({
    credentials: {},
    valid: true,
    loading: false
  }),
  methods: {
    login() {}
  }
};
</script>
