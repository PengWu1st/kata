<template>
  <div class="dynamic-array-visualizer">
    <h1>Dynamic Array Visualizer</h1>
    <div class="controls">
      <input
        v-model.number="capacity"
        type="number"
        placeholder="Enter capacity"
      />
      <button @click="initializeArray">Reset</button>
      <button @click="pushback">Push Back</button>
      <button @click="popback">Pop Back</button>
    </div>
    <div class="array">
      <div
        v-for="(item, index) in array"
        :key="index"
        :class="['array-item', { 'green-item': index < dynamicArray.size }]"
      >
        {{ item }}
      </div>
    </div>
  </div>
</template>

<script>
import DynamicArray from "./DynamicArray";

export default {
  data() {
    return {
      dynamicArray: new DynamicArray(4),
      array: [],
      capacity: 4,
    };
  },
  methods: {
    initializeArray() {
      this.dynamicArray = new DynamicArray(this.capacity);
      this.updateArray();
    },
    pushback() {
      this.dynamicArray.pushback(Math.floor(Math.random() * 100));
      this.updateArray();
    },
    popback() {
      this.dynamicArray.popback();
      this.updateArray();
    },
    updateArray() {
      this.array = this.dynamicArray._array.slice(
        0,
        this.dynamicArray.capacity
      );
    },
  },
  mounted() {
    this.updateArray();
  },
};
</script>

<style>
.dynamic-array-visualizer {
  position: fixed;
  top: 0;
  left: 0;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.controls {
  margin-bottom: 20px;
}

.array {
  display: flex;
  justify-content: left;
  flex-wrap: wrap;
}

.array-item {
  width: 50px;
  height: 50px;
  line-height: 50px;
  margin: 5px;
  background-color: #d3d3d3;
  color: white;
  font-weight: bold;
  border-radius: 5px;
}

.green-item {
  background-color: #42b983;
}
</style>
