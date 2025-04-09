let currentConfig = null;
let currentConfigName = null;
let configurations = {};

// Load configurations when the page loads
document.addEventListener('DOMContentLoaded', function() {
    loadConfigurations();
});

// Load all configurations from the server
function loadConfigurations() {
    fetch('/api/controller/configs')
        .then(response => response.json())
        .then(data => {
            configurations = data;
            renderConfigList();
            if (currentConfigName) {
                loadConfigForEditing(currentConfigName);
            }
            const firstConfig = configurations[0];
            if (firstConfig) {
                loadConfigForEditing(firstConfig);
            }
        })
        .catch(error => {
            console.error('Error loading configurations:', error);
            alert('Error loading configurations');
        });
}

// Render the list of configurations
function renderConfigList() {
    const configList = document.getElementById('configList');
    configList.innerHTML = '';

    configurations.forEach(configName => {
        const div = document.createElement('div');
        div.className = `config-item ${configName === currentConfigName ? 'active' : ''}`;
        div.textContent = configName;
        div.onclick = () => loadConfigForEditing(configName);
        configList.appendChild(div);
    });
}

// Load a configuration into the editor
function loadConfigForEditing(configName) {
    // Fetch the configuration from the server
    fetch(`/api/controller/configs/${configName}`)
    .then(response => response.json())
    .then(config => {
        currentConfig = config;
        currentConfigName = configName;
        console.log('Configuration loaded:', config);

        // Update the config name in the input field
        document.getElementById('configName').value = configName;
        
        // Load linear axes
        ['x', 'y', 'z'].forEach(axis => {
            const linearConfig = config.joystick.linear[axis];
            document.getElementById(`linear-${axis}-device`).value = linearConfig.device;
            document.getElementById(`linear-${axis}-axis`).value = linearConfig.axis;
            document.getElementById(`linear-${axis}-scale`).value = linearConfig.scale;
            document.getElementById(`linear-${axis}-invert`).checked = linearConfig.invert;
        });
        
        // Load angular axes
        ['x', 'y', 'z'].forEach(axis => {
            const angularConfig = config.joystick.angular[axis];
            document.getElementById(`angular-${axis}-device`).value = angularConfig.device;
            document.getElementById(`angular-${axis}-axis`).value = angularConfig.axis;
            document.getElementById(`angular-${axis}-scale`).value = angularConfig.scale;
            document.getElementById(`angular-${axis}-invert`).checked = angularConfig.invert;
        });
        
        // Load button mappings
        // renderButtonMappings(config.buttons.tool_toggle);
        
        // Load other settings
        document.getElementById('deadZone').value = config.dead_zone;
        
        // Update UI
        renderConfigList();
    })
    .catch(error => {
        console.error('Error loading configuration:', error);
        alert('Error loading configuration');
    });
}

// Save the current configuration
function saveCurrentConfig(saveName) {
    if (!currentConfig) return;
    
    // const newName = document.getElementById('configName').value.trim();
    if (!saveName) {
        alert('Configuration name cannot be empty.');
        return;
    }
    if (/\s/.test(saveName)) {
        alert('Configuration name cannot contain spaces.');
        return;
    }
    const config = {
        joystick: {
            linear: {},
            angular: {}
        },
        buttons: {
            tool_toggle: []
        },
        trims: { x: 0.0, y: 0.0, z: 0.0 },
        dead_zone: parseFloat(document.getElementById('deadZone').value),
        scale_factors: {
            translational_x: 1.0,
            translational_y: 1.0,
            translational_z: 1.0,
            rotational_x: 1.0,
            rotational_y: 1.0,
            rotational_z: 1.0
        }
    };
    
    // Gather linear axes configuration
    ['x', 'y', 'z'].forEach(axis => {
        config.joystick.linear[axis] = {
            device: document.getElementById(`linear-${axis}-device`).value,
            axis: parseInt(document.getElementById(`linear-${axis}-axis`).value),
            scale: parseFloat(document.getElementById(`linear-${axis}-scale`).value),
            invert: document.getElementById(`linear-${axis}-invert`).checked
        };
    });
    
    // Gather angular axes configuration
    ['x', 'y', 'z'].forEach(axis => {
        config.joystick.angular[axis] = {
            device: document.getElementById(`angular-${axis}-device`).value,
            axis: parseInt(document.getElementById(`angular-${axis}-axis`).value),
            scale: parseFloat(document.getElementById(`angular-${axis}-scale`).value),
            invert: document.getElementById(`angular-${axis}-invert`).checked
        };
    });
    
    // Gather button mappings
    // config.buttons.tool_toggle = getButtonMappings();
    
    // Send to server
    fetch('/api/controller/configs/' + saveName, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(config)
    })
    .then(response => {
        if (response.ok) {
            console.log('Configuration saved successfully:', saveName);
            loadConfigurations();
        } else {
            console.error('Failed to save configuration:', response.statusText);
            alert('Failed to save configuration');
        }
    })
    .catch(error => {
        console.error('Error saving configuration:', error);
        alert('Error saving configuration');
    });
}

// Create a new configuration
function createNewConfig() {
    const name = prompt('Enter a name for the new configuration:');
    if (!name) return;
    
    const defaultConfig = {
        joystick: {
            linear: {
                x: {"device": "joystick_left", "axis": 1, "scale": 1.0, "invert": false},
                y: {"device": "joystick_left", "axis": 0, "scale": 1.0, "invert": false},
                z: {"device": "joystick_right", "axis": 2, "scale": 1.0, "invert": false}
            },
            angular: {
                x: {"device": "joystick_right", "axis": 1, "scale": 1.0, "invert": false},
                y: {"device": "joystick_right", "axis": 0, "scale": 1.0, "invert": false},
                z: {"device": "joystick_left", "axis": 2, "scale": 1.0, "invert": false}
            }
        },
        buttons: {
            tool_toggle: []
        },
        trims: { x: 0.0, y: 0.0, z: 0.0 },
        dead_zone: 0.09,
        scale_factors: {
            translational_x: 1.0,
            translational_y: 1.0,
            translational_z: 1.0,
            rotational_x: 1.0,
            rotational_y: 1.0,
            rotational_z: 1.0
        }
    };

    currentConfig = defaultConfig;
    currentConfigName = name;
    saveCurrentConfig(currentConfigName);
    console.log('New configuration created:', name);
    loadConfigForEditing(currentConfigName);
}

// Delete the current configuration
function deleteCurrentConfig() {
    if (!currentConfigName || !confirm(`Are you sure you want to delete the "${currentConfigName}" configuration?`)) {
        return;
    }

    fetch(`/api/controller/configs/${currentConfigName}`, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            console.log(`Configuration "${currentConfigName}" deleted successfully.`);
            delete configurations[currentConfigName];
            currentConfig = null;
            currentConfigName = null;
            loadConfigurations();
        } else {
            console.error('Failed to delete configuration:', response.statusText);
            alert('Failed to delete configuration');
        }
    })
    .catch(error => {
        console.error('Error deleting configuration:', error);
        alert('Error deleting configuration');
    });
}

// Helper functions for button mappings
function renderButtonMappings(mappings) {
    const container = document.getElementById('buttonMappings');
    container.innerHTML = '';
    
    mappings.forEach((mapping, index) => {
        container.appendChild(createButtonMappingElement(mapping, index));
    });
}

function createButtonMappingElement(mapping, index) {
    const div = document.createElement('div');
    div.className = 'mb-3 p-2 border border-secondary rounded';
    div.innerHTML = `
        <div class="row">
            <div class="col">
                <label class="form-label">Device</label>
                <select class="form-select" id="button-${index}-device">
                    <option value="joystick_left">Left Joystick</option>
                    <option value="joystick_right">Right Joystick</option>
                </select>
            </div>
            <div class="col">
                <label class="form-label">Button</label>
                <input type="number" class="form-control" id="button-${index}-button" value="${mapping.button}">
            </div>
            <div class="col">
                <label class="form-label">Action</label>
                <select class="form-select" id="button-${index}-action">
                    <option value="toggle" ${mapping.action === 'toggle' ? 'selected' : ''}>Toggle</option>
                    <option value="hold" ${mapping.action === 'hold' ? 'selected' : ''}>Hold</option>
                </select>
            </div>
            <div class="col">
                <label class="form-label">Tool ID</label>
                <input type="number" class="form-control" id="button-${index}-tool" value="${mapping.tool_id}">
            </div>
            <div class="col-auto d-flex align-items-end">
                <button type="button" class="btn btn-danger" onclick="removeButtonMapping(${index})">
                    <i class="bi bi-trash"></i>
                </button>
            </div>
        </div>
    `;
    return div;
}

function getButtonMappings() {
    const mappings = [];
    const container = document.getElementById('buttonMappings');
    const mappingElements = container.children;
    
    for (let i = 0; i < mappingElements.length; i++) {
        mappings.push({
            device: document.getElementById(`button-${i}-device`).value,
            button: parseInt(document.getElementById(`button-${i}-button`).value),
            action: document.getElementById(`button-${i}-action`).value,
            tool_id: parseInt(document.getElementById(`button-${i}-tool`).value)
        });
    }
    
    return mappings;
}

function addButtonMapping() {
    const container = document.getElementById('buttonMappings');
    const newMapping = {
        device: 'joystick_left',
        button: 0,
        action: 'toggle',
        tool_id: 0
    };
    container.appendChild(createButtonMappingElement(newMapping, container.children.length));
}

function removeButtonMapping(index) {
    const container = document.getElementById('buttonMappings');
    container.removeChild(container.children[index]);
}