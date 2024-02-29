document.getElementById('exportBtn').addEventListener('click', analyze_data);
document.getElementById("debugBtn").addEventListener('click', () => {
  exportData()
  let res = analyze_data();
  let headers = [...res.count.X, ...res.count.Y, ...res.count.Q];
  console.log(res.X_indices, res.Y_indices, res.Q_indices)
  // Generate tables for each object
  generateTableRows(res.X_indices, 'object1-table');
  generateTableRows(res.Y_indices, 'object2-table');
  generateTableRows(res.Q_indices, 'object3-table');
})

function generateTableRows(object, containerId) {
  const tbody = document.getElementById(containerId).getElementsByTagName('tbody')[0];
  tbody.innerHTML = "";
  for (const [key, value] of Object.entries(object)) {
    const row = document.createElement('tr');
    const keyCell = document.createElement('td');
    keyCell.textContent = key;
    const valueCell = document.createElement('td');
    valueCell.textContent = value.join(', '); // Join array elements with comma for display
    row.appendChild(keyCell);
    row.appendChild(valueCell);
    tbody.appendChild(row);
  }
}


zip = (...rows) => [...rows[0]].map((_, c) => rows.map(row => row[c]))

function mapToBinaryIndices(names, length) {
  const binaryIndices = {};
  for (let i = 0; i < names.length; i++) {
    binaryIndices[names[i]] = i.toString(2).padStart(length, '0').split('');
  }
  return binaryIndices;
}

function analyze_data() {
  let table_data = data || [{name: "S1", edges: [{x: "X1", y: "Y2", to: "S2"}]}, {name: "S2", edges: []}];
  console.log(table_data)
  let count = {X: [], Y: [], Q: []}
  table_data.forEach((node) => {
    let causes = node.edges.map((edge) => edge.x);
    causes.forEach((cause) => {
      if (!(count.X.includes(cause))) {
        count.X.push(cause);
      }
    })
    let actions = node.edges.map((edge) => edge.y);
    actions.forEach((action) => {
      if (!(count.Y.includes(action))) {
        count.Y.push(action);
      }
    })
    if (!(count.Q.includes(node.name))) {
      count.Q.push(node.name);
    }
  })
  const X_indices = mapToBinaryIndices(count.X, Math.ceil(Math.log2(count.X.length)));
  const Y_indices = mapToBinaryIndices(count.Y, Math.ceil(Math.log2(count.Y.length)));
  const Q_indices = mapToBinaryIndices(count.Q, Math.ceil(Math.log2(count.Q.length)));
  const headers = []
  for (const [key, value] of zip("XQqY", [
    Math.ceil(Math.log2(count.X.length)),
    Math.ceil(Math.log2(count.Q.length)),
    Math.ceil(Math.log2(count.Q.length)),
    Math.ceil(Math.log2(count.Y.length))])) {
    for (let i = 0; i < value; i++) {
      headers.push(key + (i + 1));
    }
  }
  console.log(headers);
  console.log(count);
  let result = [];
  
  table_data.forEach((node) => {
    node.edges.forEach((edge) => {
      let data = [];
      data.push(...X_indices[edge.x]);
      data.push(...Q_indices[node.name]);
      data.push(...Q_indices[edge.to]);
      data.push(...Y_indices[edge.y]);
      result.push(data);
    })
  })
  console.log(result);
  addTableToHTML(result, headers);
  return {
    count,
    X_indices,
    Y_indices,
    Q_indices
  }
}

function addTableToHTML(data, headers) {
  // Remove existing table if it exists
  const existingTable = document.getElementById('data-table');
  if (existingTable) {
    existingTable.parentNode.removeChild(existingTable);
  }

  const tableContainer = document.getElementById('data-table-container');
  tableContainer.style.float = 'right'; // Align the table to the right
  tableContainer.style.width = 'auto'; // Align the table to the right
  tableContainer.style.marginLeft = '20px'; // Add some margin between the canvas and the table
  tableContainer.style.marginRight = '20px'; // Add some margin between the canvas and the table

  const table = document.createElement('table');
  table.className = "table table-sm table-hover table-striped"
  table.id = 'data-table'; // Set an ID for the table
  table.style.borderCollapse = 'collapse';
  table.style.width = "auto";

  // Add table header
  const thead = document.createElement("thead");
  const headerRow = document.createElement('tr');
  headerRow.className = "table-active";
  headers.forEach(title => {
    const th = document.createElement('th');
    th.textContent = title;
    th.scope = "col";
    th.style.border = '1px solid black';
    th.style.padding = '8px';
    th.style.textAlign = 'center';
    headerRow.appendChild(th);
  });
  thead.appendChild(headerRow);
  table.appendChild(thead);

  // Add table rows
  const tbody = document.createElement("tbody");
  data.forEach((rowValues, index) => {
    const row = document.createElement('tr');
    rowValues.forEach(value => {
      const td = document.createElement('td');
      td.textContent = value;
      td.style.border = '1px solid black';
      td.style.padding = '8px';
      td.style.textAlign = 'center';
      row.appendChild(td);
    });
    tbody.appendChild(row);
  });

  table.appendChild(tbody);
  tableContainer.appendChild(table);

  // Append the table container to the body
}
