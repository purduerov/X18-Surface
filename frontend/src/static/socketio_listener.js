var socket = io();

// Function to handle 'count' messages from the server
socket.on('count', function(msg) {
    // Log the message to the browser console
    // console.log("New message received:", msg);

    // Update the HTML element with the new message
    document.getElementById('count-data').innerText = msg;
});

// Function to handle 'rov_velocity' messages from the server
socket.on('rov_velocity', function(msg) {
    // Log the message to the browser console
    // console.log("New message received:", msg);
    // Parse the message into json
    msg = JSON.parse(msg);

    // Insert the following x: 0<br>y: 0<br>z: 0 into the HTLM div with id linear-command
    document.getElementById("linear-command").innerHTML = "x: " + msg.twist.linear.x.toFixed(3) + "<br>y: " + msg.twist.linear.y.toFixed(3) + "<br>z: " + msg.twist.linear.z.toFixed(3);
    // Do the same thing for the angular command
    document.getElementById("angular-command").innerHTML = "Pitch: " + msg.twist.angular.x.toFixed(3) + "<br>Roll: " + msg.twist.angular.y.toFixed(3) + "<br>Yaw: " + msg.twist.angular.z.toFixed(3);
});  // Log the message to the browser console
// console.log("New message received:", msg);

// Update the HTML element with the new message
document.getElementById('count-data').innerText = msg;

socket.on('surface_imu', function(msg) {
    // Log the message to the browser console
    // console.log("New message received:", msg);
    // Parse the message into json
    msg = JSON.parse(msg);

    // Insert the following x: 0<br>y: 0<br>z: 0 into the HTLM div with id linear-command
    document.getElementById("acceleration").innerHTML = "x: " + msg.twist.linear.x.toFixed(3) + "<br>y: " + msg.twist.linear.y.toFixed(3) + "<br>z: " + msg.twist.linear.z.toFixed(3);
    // Do the same thing for the angular command
    document.getElementById("angular-command").innerHTML = "Pitch: " + msg.twist.angular.x.toFixed(3) + "<br>Roll: " + msg.twist.angular.y.toFixed(3) + "<br>Yaw: " + msg.twist.angular.z.toFixed(3);
});

// Handle socket connection and disconnection events
socket.on('connect', function() {
    console.log("Socket connected");
});

socket.on('disconnect', function() {
    console.log("Socket disconnected");
});