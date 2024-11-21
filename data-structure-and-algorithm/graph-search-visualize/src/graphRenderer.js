import { graph } from './graph';

export function createGraphElements(container) {
  createEdges(container);
  createNodes(container);
}

function createEdges(container) {
  graph.edges.forEach(([from, to]) => {
    const edge = document.createElement('div');
    edge.className = 'edge';
    
    const fromNode = graph.nodes[from];
    const toNode = graph.nodes[to];
    
    const length = Math.sqrt(
      Math.pow(toNode.x - fromNode.x, 2) + 
      Math.pow(toNode.y - fromNode.y, 2)
    );
    
    const angle = Math.atan2(
      toNode.y - fromNode.y,
      toNode.x - fromNode.x
    ) * 180 / Math.PI;
    
    edge.style.width = `${length}px`;
    edge.style.left = `${fromNode.x + 20}px`;
    edge.style.top = `${fromNode.y + 20}px`;
    edge.style.transform = `rotate(${angle}deg)`;
    
    container.appendChild(edge);
  });
}

function createNodes(container) {
  graph.nodes.forEach(node => {
    const element = document.createElement('div');
    element.className = 'node';
    element.id = `node-${node.id}`;
    element.textContent = node.id;
    element.style.left = `${node.x}px`;
    element.style.top = `${node.y}px`;
    container.appendChild(element);
  });
}

export function findEdgeElement(from, to) {
  const edges = document.getElementsByClassName('edge');
  const fromNode = graph.nodes[from];
  const toNode = graph.nodes[to];
  
  const angle = Math.atan2(
    toNode.y - fromNode.y,
    toNode.x - fromNode.x
  ) * 180 / Math.PI;
  
  for (const edge of edges) {
    const edgeAngle = getRotationAngle(edge);
    if (Math.abs(edgeAngle - angle) < 1 || Math.abs(edgeAngle - angle - 180) < 1) {
      return edge;
    }
  }
  return null;
}

function getRotationAngle(element) {
  const style = window.getComputedStyle(element);
  const transform = style.getPropertyValue('transform');
  const values = transform.split('(')[1].split(')')[0].split(',');
  const a = values[0];
  const b = values[1];
  return Math.round(Math.atan2(b, a) * (180/Math.PI));
}