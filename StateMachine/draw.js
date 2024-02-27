const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

const Default = () => {
  const node0 = {x: 217, y: 70.13333129882812, name: "S0", edges: []};
  const node1 = {x: 430, y: 121.13333129882812, name: "S1", edges: []};
  const node2 = {x: 219, y: 289.1333312988281, name: "S2", edges: []};
  const node3 = {x: 470, y: 306.1333312988281, name: "S3", edges: []};
  const node4 = {x: 421, y: 448.1333312988281, name: "S4", edges: []};
  node0.edges.push({end: node1, a: "X0", b: "Y0"});

  node1.edges.push({end: node1, a: "X0", b: "Y0"});
  node1.edges.push({end: node3, a: "X2", b: "Y5"});
  node1.edges.push({end: node2, a: "X1", b: "Y1"});

  node2.edges.push({end: node2, a: "X0", b: "Y2"});
  node2.edges.push({end: node0, a: "X1", b: "Y3"});

  node3.edges.push({end: node4, a: "X2", b: "Y3"});
  node3.edges.push({end: node3, a: "X0", b: "Y0"});
  node3.edges.push({end: node2, a: "X1", b: "Y4"});

  node4.edges.push({end: node2, a: "X0", b: "Y2"});
  node4.edges.push({end: node4, a: "X1", b: "Y1"});
  return [node0, node1, node2, node3, node4];
}

let nodes = Default();
let draggedNode = null;
let edgeStartNode = null;
let data;

const RADIUS = 30;
const rotateVector = function (vec, ang) {
  ang = -ang * (Math.PI / 180);
  const cos = Math.cos(ang);
  const sin = Math.sin(ang);
  return {
    x: Math.round(10000 * (vec.x * cos - vec.y * sin)) / 10000,
    y: Math.round(10000 * (vec.x * sin + vec.y * cos)) / 10000
  };
};

function drawNode(x, y, name) {
  ctx.beginPath();
  ctx.arc(x, y, RADIUS, 0, Math.PI * 2);
  ctx.fillStyle = '#0095DD';
  ctx.fill();
  ctx.fillStyle = 'white';
  ctx.font = 'bold 12px Arial';
  ctx.textAlign = 'center';
  ctx.fillText(name, x, y + 4);
  ctx.closePath();
}

function drawEdge(x1, y1, x2, y2, a, b) {
  let [dx, dy] = [x2 - x1, y2 - y1];

  let distance = (dx * dx + dy * dy) ** 0.5 + 0.0001;
  let center = {
    x: (x1 + x2) / 2,
    y: (y1 + y2) / 2
  }
  const direction = {x: dx / distance, y: dy / distance};
  ctx.beginPath();
  const offset_direction = rotateVector(direction, 30);
  if (dx === 0 && dy === 0) {
    const def = {x: 1, y: 0};
    ctx.moveTo(x1 + def.x * RADIUS, y1 + def.y * RADIUS);
    const rot = rotateVector(def, 45);
    const rot2 = rotateVector(def, -45);
    ctx.bezierCurveTo(
      x1 + rot.x * RADIUS * 3, y1 + rot.y * RADIUS * 3,
      x1 + rot2.x * RADIUS * 3, y1 + rot2.y * RADIUS * 3,
      x1 + def.x * RADIUS, y1 + def.y * RADIUS)
    center = {
      x: (x1 + rot.x * RADIUS * 3 + x1 + rot2.x * RADIUS * 3) / 2,
      y: (y1 + rot.y * RADIUS * 3 + y1 + rot2.y * RADIUS * 3) / 2
    }
  } else {
    ctx.moveTo(x1 + direction.x * RADIUS, y1 + direction.y * RADIUS);
    ctx.quadraticCurveTo(
      x1 + direction.x * RADIUS + offset_direction.x * 100,
      y1 + direction.y * RADIUS + offset_direction.y * 100,
      x2 - direction.x * RADIUS,
      y2 - direction.y * RADIUS)
  }
  // ctx.lineTo(x2 - direction.x * RADIUS, y2 - direction.y * RADIUS);
  ctx.strokeStyle = '#FF0000';
  ctx.lineWidth = 2;
  ctx.stroke();

  // Draw arrowhead
  if (dx === 0 && dy === 0) {

  } else {
    const angle = Math.atan2(y2 - y1, x2 - x1);
    ctx.save();
    ctx.translate(x2 - direction.x * RADIUS, y2 - direction.y * RADIUS);
    ctx.rotate(angle);
    ctx.beginPath();
    ctx.moveTo(-10, -5);
    ctx.lineTo(0, 0);
    ctx.lineTo(-10, 5);
    ctx.fillStyle = '#FF0000';
    ctx.fill();
    ctx.restore();
  }
  // Draw text
  ctx.fillStyle = '#000000';
  ctx.font = '12px Arial';
  ctx.textAlign = 'center';
  ctx.fillText(a, center.x, center.y - 10);
  ctx.fillText(b, center.x, center.y + 10);
}

function clearCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function redraw() {
  clearCanvas();
  nodes.forEach(node => {
    drawNode(node.x, node.y, node.name);
  });
  nodes.forEach(node => {
    node.edges.forEach(edge => {
      drawEdge(node.x, node.y, edge.end.x, edge.end.y, edge.a, edge.b);
    });
  });
}

function exportData() {
  data = nodes.map(node => {
    const edges = node.edges.map(edge => {
      return {x: edge.a, y: edge.b, to: edge.end.name};
    });
    return {name: node.name, edges};
  });
}

canvas.addEventListener('mousedown', (e) => {
  const rect = canvas.getBoundingClientRect();
  const mouseX = e.clientX - rect.left;
  const mouseY = e.clientY - rect.top;
  const clickedNode = nodes.find(node => {
    const dx = mouseX - node.x;
    const dy = mouseY - node.y;
    return dx * dx + dy * dy < RADIUS * RADIUS;
  });
  if (clickedNode) {
    if (e.button === 2) {
      draggedNode = clickedNode;
    } else if (e.button === 1) {
      nodes = nodes.filter(node => {
        node.edges = node.edges.filter(edge => edge.end.name !== clickedNode.name)
        return node.name !== clickedNode.name
      })
      redraw();
    } else if (e.button === 0) {
      if (!edgeStartNode) {
        edgeStartNode = clickedNode;
      } else {
        edgeStartNode.edges.push({
          end: clickedNode,
          a: prompt('Введите свойство X:') || '',
          b: prompt('Введите свойство Y:') || ''
        });
        edgeStartNode = null;
        redraw();
      }
    }
  } else {
    if (e.button === 0) {
      nodes.push({x: mouseX, y: mouseY, name: prompt('Enter node name:') || '', edges: []});
      redraw();
    }
  }
});

canvas.addEventListener('mousemove', (e) => {
  if (edgeStartNode) {
    const rect = canvas.getBoundingClientRect();
    redraw();
    drawEdge(edgeStartNode.x, edgeStartNode.y, e.clientX - rect.left, e.clientY - rect.top, "", "");
  }

  if (draggedNode) {
    const rect = canvas.getBoundingClientRect();
    draggedNode.x = e.clientX - rect.left;
    draggedNode.y = e.clientY - rect.top;
    redraw();
  }
});

canvas.addEventListener('mouseup', () => {
  draggedNode = null;
});

document.getElementById('exportBtn').addEventListener('click', exportData);
redraw();
