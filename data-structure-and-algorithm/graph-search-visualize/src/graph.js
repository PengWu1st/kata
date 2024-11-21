// Graph data structure
export const graph = {
  nodes: [
    { id: 0, x: 400, y: 50 },
    { id: 1, x: 200, y: 150 },
    { id: 2, x: 600, y: 150 },
    { id: 3, x: 100, y: 250 },
    { id: 4, x: 300, y: 250 },
    { id: 5, x: 500, y: 250 },
    { id: 6, x: 700, y: 250 },
  ],
  edges: [
    [0, 1],
    [0, 2],
    [1, 3],
    [1, 4],
    [2, 5],
    [2, 6],
  ],
};

// Graph traversal algorithms with stack/queue tracking
export function* dfs(start = 0) {
  const visited = new Set();
  const stack = [start];
  yield {
    node: null,
    dataStructure: [...stack],
    visited: new Set(visited),
  };

  while (stack.length > 0) {
    const current = stack.pop();

    if (!visited.has(current)) {
      visited.add(current);

      const neighbors = getNeighbors(current)
        .filter((neighbor) => !visited.has(neighbor))
        .reverse();

      stack.push(...neighbors);
      // for (const neighbor of neighbors) {
      //   stack.push(neighbor);
      // }
      // Yield current node, stack state, and visited nodes
      yield {
        node: current,
        dataStructure: [...stack],
        visited: new Set(visited),
      };
    }
  }
}

export function* bfs(start = 0) {
  const visited = new Set();
  const queue = [start];
  yield {
    node: null,
    dataStructure: [...queue],
    visited: new Set(visited),
  };

  while (queue.length > 0) {
    const current = queue.shift();

    if (!visited.has(current)) {
      visited.add(current);

      const neighbors = getNeighbors(current).filter(
        (neighbor) => !visited.has(neighbor)
      );

      queue.push(...neighbors);

      // Yield current node, queue state, and visited nodes
      yield {
        node: current,
        dataStructure: [...queue],
        visited: new Set(visited),
      };
    }
  }
}

function getNeighbors(node) {
  return graph.edges
    .filter(([from, to]) => from === node || to === node)
    .map(([from, to]) => (from === node ? to : from));
}
