<template>
  <div class="screen" @drop="onDrop" @dragover="onDragOver">
    <vue-draggable-resizable
      v-for="(icon, index) in icons"
      :key="index"
      :x="icon.x"
      :y="icon.y"
      @dragging="onDragging(icon, $event)"
    >
      <img :src="icon.src" class="icon" />
    </vue-draggable-resizable>
  </div>
</template>

<script>
import VueDraggableResizable from "vue-draggable-resizable";
import "vue-draggable-resizable/dist/VueDraggableResizable.css";
import { Point, Rectangle, QuadTree } from "../QuadTree";

export default {
  components: {
    VueDraggableResizable,
  },
  data() {
    return {
      icons: [
        { x: 50, y: 50, src: "icon1.png" },
        { x: 150, y: 150, src: "icon2.png" },
      ],
      quadTree: null,
    };
  },
  mounted() {
    let boundary = new Rectangle(0, 0, 400, 800);
    this.quadTree = new QuadTree(boundary, 4);
    this.icons.forEach((icon) => {
      let point = new Point(icon.x, icon.y, icon);
      this.quadTree.insert(point);
    });
  },
  methods: {
    onDragOver(event) {
      event.preventDefault();
    },
    onDrop(event) {
      event.preventDefault();
    },
    onDragging(icon, event) {
      let point = new Point(event.x, event.y, icon);
      this.quadTree.insert(point);
    },
  },
};
</script>

<style>
.screen {
  width: 400px;
  height: 800px;
  border: 1px solid #000;
  position: relative;
}
.icon {
  width: 50px;
  height: 50px;
}
</style>
