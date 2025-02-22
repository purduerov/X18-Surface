var socket = io();

// Function to update the status of a node
function updateNodeStatus(nodeName, status, location) {
    const tableId = location === 'surface' ? 'surface-node-table' : 'core-node-table';
    const table = document.getElementById(tableId).getElementsByTagName('tbody')[0];
    let row = document.getElementById(nodeName);

    if (!row) {
        // Create a new row if the node doesn't exist
        row = document.createElement('tr');
        row.id = nodeName;

        const nameCell = document.createElement('td');
        nameCell.textContent = nodeName;
        row.appendChild(nameCell);

        const statusCell = document.createElement('td');
        statusCell.className = status === 'active' ? 'active' : 'inactive';
        statusCell.textContent = status;
        row.appendChild(statusCell);

        table.appendChild(row);
    } else {
        // Update the status of the existing node
        const statusCell = row.getElementsByTagName('td')[1];
        statusCell.className = status === 'active' ? 'active' : 'inactive';
        statusCell.textContent = status;
    }

    // Sort the rows alphabetically by node name
    const rows = Array.from(table.getElementsByTagName('tr'));
    rows.sort((a, b) => a.id.localeCompare(b.id));
    rows.forEach(row => table.appendChild(row));
}

// Handle socket connection and disconnection events
socket.on('connect', function() {
    console.log("Socket connected");
});

socket.on('disconnect', function() {
    console.log("Socket disconnected");

    // Set all nodes to inactive
    ['surface-node-table', 'core-node-table'].forEach(tableId => {
        const table = document.getElementById(tableId).getElementsByTagName('tbody')[0];
        const rows = table.getElementsByTagName('tr');
        for (let row of rows) {
            const statusCell = row.getElementsByTagName('td')[1];
            statusCell.className = 'inactive';
            statusCell.textContent = 'inactive';
        }
    });
});

// Handle the 'heartbeat' event
socket.on('heartbeat', function(msg) {
    // Turn the message into a JSON object
    msg = JSON.parse(msg);
    updateNodeStatus(msg.node, msg.status, msg.location);
});