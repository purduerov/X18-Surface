var socket = io();

let isSending = false;
let sendInterval = null;
let displayMode = "absolute";
let NEUTRAL_VALUE = 127;

// --------- PAGE SPECIFIC FUNCTIONS --------- //

function updateAllValues() {
    const masterValue = document.getElementById('master-slider').value;
    document.getElementById('master-slider-value').textContent = masterValue;
    for (let i = 1; i <= 8; i++) {
        toggleThrusterInput(`thruster${i}`);
    }
}

function toggleAllCheckboxes() {
    const selectAll = document.getElementById('select-all').checked;
    for (let i = 1; i <= 8; i++) {
        const checkbox = document.getElementById(`thruster${i}-check`);
        checkbox.checked = selectAll;
        toggleThrusterInput(`thruster${i}`);
    }
}

function toggleThrusterInput(thruster) {
    const checkbox = document.getElementById(`${thruster}-check`);
    const input = document.getElementById(thruster);
    input.readOnly = checkbox.checked;
    if (checkbox.checked) {
        const masterValue = document.getElementById('master-slider').value;
        input.value = masterValue;
    }
}

function resetValues() {
    const defaultValue = displayMode === "absolute" ? 127 : 0;
    // Stop continuous sending if active
    if(isSending) {
        clearInterval(sendInterval);
        isSending = false;
        document.getElementById("toggle-send").textContent = "Send Values";
        document.getElementById("toggle-send").className = "btn btn-primary";
        document.getElementById("send-once").style.display = "inline-block";
    }
    // Reset master slider and its display
    document.getElementById('master-slider').value = defaultValue;
    document.getElementById('master-slider-value').value = defaultValue;
    // Uncheck the select-all checkbox
    document.getElementById('select-all').checked = false;
    // Reset each thruster input and checkbox
    for (let i = 1; i <= 8; i++) {
        const input = document.getElementById(`thruster${i}`);
        const checkbox = document.getElementById(`thruster${i}-check`);
        input.value = defaultValue;
        input.readOnly = false;
        checkbox.checked = false;
    }
}

function toggleSendValues() {
    const toggleBtn = document.getElementById("toggle-send");
    const sendOnceBtn = document.getElementById("send-once");
    if (!isSending) {
        // Start sending continuously
        isSending = true;
        toggleBtn.textContent = "Stop Sending Values";
        toggleBtn.className = "btn btn-danger";
        sendOnceBtn.style.display = "none";
        sendInterval = setInterval(sendThrusterValues, 500); // Adjust interval as needed
    } else {
        // Stop continuous sending
        isSending = false;
        toggleBtn.textContent = "Send Values";
        toggleBtn.className = "btn btn-primary";
        sendOnceBtn.style.display = "inline-block";
        clearInterval(sendInterval);
    }
}

function updateFinalThrustDisplay(thrusters) {
    thrusters = JSON.parse(thrusters).thrusters;
    for (let i = 1; i <= 8; i++) {
        const id = `final-thrust${i}`;
        if (thrusters[i - 1] !== undefined) {
            document.getElementById(id).textContent = thrusters[i - 1].toString();
        }
    }
}

function updateAllValues() {
    const masterValue = document.getElementById('master-slider').value;
    // Update textbox value since it's now editable
    document.getElementById('master-slider-value').value = masterValue;
    for (let i = 1; i <= 8; i++) {
        toggleThrusterInput(`thruster${i}`);
    }
}

function updateSliderFromTextbox() {
    const newVal = document.getElementById('master-slider-value').value;
    document.getElementById('master-slider').value = newVal;
    updateAllValues();
}

function toggleDisplayMode() {
    // If the display mode is 
    let displayModeLabel = document.getElementById('display-mode-label');
    if (displayMode === "absolute") {
        displayMode = "relative";
        displayModeLabel.textContent = "Relative (-127 - 127)";

        // Update all input fields to show relative values
        for (let i = 1; i <= 8; i++) {
            const input = document.getElementById(`thruster${i}`);
            const currentValue = parseInt(input.value);
            input.value = currentValue - NEUTRAL_VALUE;
            input.min = -127;
            input.max = 128;
        }

        // Update master slider
        const masterSlider = document.getElementById('master-slider');
        const masterValue = document.getElementById('master-slider-value');
        masterSlider.min = -127;
        masterSlider.max = 128;
        masterSlider.value = parseInt(masterValue.value) - NEUTRAL_VALUE;
        masterValue.value = masterSlider.value;

    } else {
        displayMode = "absolute";
        displayModeLabel.textContent = "Absolute (0 - 255)";

        // Update all input fields to show absolute values
        for (let i = 1; i <= 8; i++) {
            const input = document.getElementById(`thruster${i}`);
            const currentValue = parseInt(input.value);
            input.value = currentValue + 127;
            input.min = 0;
            input.max = 255;
        }

        // Update master slider
        const masterSlider = document.getElementById('master-slider');
        const masterValue = document.getElementById('master-slider-value');
        masterSlider.min = 0;
        masterSlider.max = 255;
        masterSlider.value = parseInt(masterValue.value) + NEUTRAL_VALUE;
        masterValue.value = masterSlider.value;
    }
}

// --------- SOCKETIO FUNCTIONS --------- //
// Handle socket connection and disconnection events
socket.on('connect', function() {
    console.log("Socket connected");
});

socket.on('disconnect', function() {
    console.log("Socket disconnected");
});

// Handle the 'heartbeat' event
// socket.on('heartbeat', function(msg) {
//     // Turn the message into a JSON object
//     msg = JSON.parse(msg);
//     updateNodeStatus(msg.node, msg.status, msg.location);
// });

// Update final thrust display when a "final_thrust" message is received.
socket.on('/final_thrust', function(msg) {
    console.log("New message received:", msg);
    updateFinalThrustDisplay(msg);
});

// Dummy send once function (can be modified as needed)
function sendThrusterValues() {
    // Get the values from the input fields
    const thrusterValues = {
        thruster1: parseInt(document.getElementById('thruster1').value, 10),
        thruster2: parseInt(document.getElementById('thruster2').value, 10),
        thruster3: parseInt(document.getElementById('thruster3').value, 10),
        thruster4: parseInt(document.getElementById('thruster4').value, 10),
        thruster5: parseInt(document.getElementById('thruster5').value, 10),
        thruster6: parseInt(document.getElementById('thruster6').value, 10),
        thruster7: parseInt(document.getElementById('thruster7').value, 10),
        thruster8: parseInt(document.getElementById('thruster8').value, 10)
    };
    // Check if we are in absolute or relative mode
    if (displayMode === "relative") {
        for (let i = 1; i <= 8; i++) {
            thrusterValues[`thruster${i}`] += NEUTRAL_VALUE;
        }
    }
    // Send the thruster values to the backend
    socket.emit('frontend-sendThrusterValues', thrusterValues);
}
