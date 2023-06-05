<template>
  <div>
    <button @click="fetchMessage">Pobierz wiadomość z serwera</button>
    <p>{{ message }}</p>
  </div>
</template>
  
<script lang="ts">
  import { Component, Vue } from 'vue-facing-decorator';
  import axios from 'redaxios';
  
  @Component
  export default class TestFetcher extends Vue {
    message: string = '...';
  
    async fetchMessage() {
      await axios.get('api/test').then(res => {
        this.message = res.data['message'];
        console.log(res.data);
      }).catch(_ => this.message = 'Problem z przechwyceniem informacji.');
    }
  }
</script>