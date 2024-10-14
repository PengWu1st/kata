<template>
  <div id="app">
    <DragDropIcons />
  </div>
</template>

<script>
import DragDropIcons from "./components/DragDropIcons.vue";

export default {
  name: "App",
  components: {
    DragDropIcons,
  },
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
