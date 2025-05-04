<template>

  <div id="app">
    <ItemsX />
  </div>

</template>

<script>

import ItemsX from './components/ItemsX.vue';
export default {
  name: 'App',
  components: {
    ItemsX
  }
};

</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

</style>