import anime from "animejs";
import { findEdgeElement } from "./graphRenderer";

let animationSpeed = 1;

export function setAnimationSpeed(speed) {
  animationSpeed = speed;
}

export function animateTraversal(iterator) {
  return new Promise((resolve) => {
    const timeline = anime.timeline({
      easing: "easeInOutQuad",
      duration: 500 / animationSpeed,
      complete: resolve,
    });

    let previousNode = null;
    let previousDataStructure = [];
    const itemsContainer = document.getElementById("items");

    // Reset animation state
    anime.remove(".stack-item");
    itemsContainer.innerHTML = "";
    timeline.pause();

    // Convert iterator to array to prevent consumption issues
    const steps = Array.from(iterator);

    steps.forEach(({ node, dataStructure, visited }, stepIndex) => {
      const nodeElement = document.getElementById(`node-${node}`);
      const timelineOffset = (stepIndex * 1000) / animationSpeed;

      // Update stack/queue items
      timeline.add(
        {
          begin: () => {
            // Find items to add and remove
            const itemsToAdd = dataStructure.filter(
              (item) => !previousDataStructure.includes(item)
            );
            const itemsToRemove = previousDataStructure.filter(
              (item) => !dataStructure.includes(item)
            );

            // Remove items that are no longer in the structure
            const existingItems =
              itemsContainer.querySelectorAll(".stack-item");
            existingItems.forEach((item) => {
              const nodeId = parseInt(item.textContent);
              if (itemsToRemove.includes(nodeId)) {
                anime({
                  targets: item,
                  opacity: [1, 0],
                  translateX: [0, 20],
                  duration: 300 / animationSpeed,
                  easing: "easeOutCubic",
                  complete: () => item.remove(),
                });
              }
            });

            // Add new items
            itemsToAdd.forEach((item) => {
              const itemElement = document.createElement("div");
              itemElement.className = "stack-item";
              itemElement.style.opacity = "0";
              itemElement.style.transform = "translateX(-20px)";
              itemElement.textContent = `${item}`;

              // Insert at the correct position
              const position = dataStructure.indexOf(item);
              const currentItems = itemsContainer.children;

              if (position >= currentItems.length) {
                itemsContainer.appendChild(itemElement);
              } else {
                itemsContainer.insertBefore(
                  itemElement,
                  currentItems[position]
                );
              }

              anime({
                targets: itemElement,
                opacity: [0, 1],
                translateX: [-20, 0],
                duration: 500 / animationSpeed,
                easing: "easeOutCubic",
                // delay: 500 / animationSpeed,
              });
            });

            previousDataStructure = [...dataStructure];
          },
          duration: 1,
        },
        timelineOffset
      );

      // Update visited nodes container
      timeline.add(
        {
          begin: () => {
            const visitedNodesContainer =
              document.getElementById("visited-nodes");
            const nodeElement = document.createElement("div");
            nodeElement.className = "visited-node";
            nodeElement.textContent = `${node}`;
            if (node !== null) {
              visitedNodesContainer.appendChild(nodeElement);
            }
          },
          duration: 1,
        },
        timelineOffset
      );

      // Highlight current node
      timeline.add(
        {
          targets: nodeElement,
          backgroundColor: "#ff0000",
          scale: 1.2,
          duration: 500 / animationSpeed,
        },
        timelineOffset
      );

      // Mark the node as visited (gray) after highlighting
      timeline.add(
        {
          targets: nodeElement,
          backgroundColor: "#808080",
          duration: 300 / animationSpeed,
        },
        timelineOffset + 500 / animationSpeed
      );

      // Mark all visited nodes as gray
      visited.forEach((visitedNode) => {
        const visitedNodeElement = document.getElementById(
          `node-${visitedNode}`
        );
        timeline.add(
          {
            targets: visitedNodeElement,
            backgroundColor: "#808080",
            duration: 300 / animationSpeed,
          },
          timelineOffset
        );
      });

      previousNode = node;
    });

    timeline.play();
  });
}
