var socket = io();

// Function to handle 'count' messages from the server
socket.on('count', function(msg) {
    // Log the message to the browser console
    console.log("New message received:", msg);

    // Update the HTML element with the new message
    document.getElementById('count-data').innerText = msg;
});

// Function to handle 'rov_velocity' messages from the server
socket.on('rov_velocity', function(msg) {
    // Log the message to the browser console
    console.log("New message received:", msg);

    // Update the HTML element with the new message
    document.getElementById('rov-velocity-data').innerText = JSON.stringify(msg);
});

// Handle socket connection and disconnection events
socket.on('connect', function() {
    console.log("Socket connected");
});

socket.on('disconnect', function() {
    console.log("Socket disconnected");
});