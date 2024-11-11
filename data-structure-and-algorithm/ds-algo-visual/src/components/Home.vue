<template>
  <div class="home">
    <h1>Data Structure and Algorithm Visualizer</h1>
    <p>
      Welcome to the Data Structure and Algorithm Visualizer. Select a topic
      below to start visualizing!
    </p>
    <ul>
      <li><router-link to="/dynamic-array">Dynamic Arrays</router-link></li>
      <li><router-link to="/linked-lists">Linked Lists</router-link></li>
      <li><router-link to="/stacks">Stacks</router-link></li>
      <li><router-link to="/queues">Queues</router-link></li>
      <li><router-link to="/trees">Trees</router-link></li>
      <li><router-link to="/graphs">Graphs</router-link></li>
      <li>
        <router-link to="/sorting-algorithms">Sorting Algorithms</router-link>
      </li>
      <li>
        <router-link to="/searching-algorithms"
          >Searching Algorithms</router-link
        >
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Home",
};
</script>

<style scoped>
.home {
  text-align: center;
  margin-top: 50px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 10px 0;
}

a {
  text-decoration: none;
  color: #42b983;
}

a:hover {
  text-decoration: underline;
}
</style>
