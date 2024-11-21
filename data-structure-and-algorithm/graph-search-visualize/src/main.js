import { createGraphElements } from "./graphRenderer";
import { animateTraversal, setAnimationSpeed } from "./animator";
import { dfs, bfs } from "./graph";

// Initialize graph
const graphContainer = document.getElementById("graph");
createGraphElements(graphContainer);

// Initialize speed control
const speedSlider = document.getElementById("speedSlider");
const speedValue = document.getElementById("speedValue");

speedSlider.addEventListener("input", (e) => {
  const speed = parseFloat(e.target.value);
  speedValue.textContent = `${speed.toFixed(1)}x`;
  setAnimationSpeed(speed);
});

// Add click handlers
document.getElementById("startDFS").addEventListener("click", () => {
  startAnimation(dfs(0));
});

document.getElementById("startBFS").addEventListener("click", () => {
  startAnimation(bfs(0));
});

document.getElementById("reset").addEventListener("click", () => {
  resetGraph();
});

function startAnimation(iterator) {
  const resetButton = document.getElementById("reset");
  resetButton.disabled = true;
  animateTraversal(iterator).then(() => {
    resetButton.disabled = false;
  });
}

function resetGraph() {
  const allNodes = document.querySelectorAll(".node");
  allNodes.forEach((nodeElement) => {
    nodeElement.style.backgroundColor = "#4a90e2";
    nodeElement.style.transform = "scale(1)";
  });

  const itemsContainer = document.getElementById("items");
  itemsContainer.innerHTML = "";

  const visitedNodesContainer = document.getElementById("visited-nodes");
  visitedNodesContainer.innerHTML = "";
}
