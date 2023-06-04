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
  class CatOrDog extends Vue {
    message: string = '';
  
    async fetchMessage() {
      try {
        await axios.get('api/test').then(res => {
          this.message = res.data['message'];
          console.log(res.data);
        });
      } catch (error) {
        console.error('Błąd podczas pobierania wiadomości z serwera', error);
      }
    }
  }

  export default CatOrDog 
  </script>