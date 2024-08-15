<template>
    <div class="container">
      <button type="button" class="btn btn-primary">{{ msg }}</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    name: 'Ping',
    data() {
      return {
        msg: '',
      };
    },
    methods: {
        getMessage() {
            axios.get('http://localhost:8000/ping')
            .then((response) => {
                this.msg = response.data;
            })
            .catch((error) => {
                console.error(error);
            });
        }
    },
    created() {
        this.getMessage();
    }
  };
  </script>