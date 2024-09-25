# X17-Surface PHOENIX BRANCH

This is the phoenix branch for X17-Surface. It is a rewrite of the previous X17-Surface codebase, with a focus on readability and maintainability. I will try to remove as much unnecessary complexity as possible while still maintaining the core functionality.

> [!WARNING]
> This branch is still a work in progress and is not yet fully functional. Do not merge into main until sufficient testing has been completed.

### Changes Made

#### 1. New .devcontainer setup
This will allow for easier development in a consistent environment.
Requires the following components to be installed on your machine:
- Docker Desktop
- Visual Studio Code
- Visual Studio Code Dev Containers extension

When all of the above are installed, you can open the project in Visual Studio Code and it will prompt you to reopen in a container. If you are not prompted, you can use the command palette (Ctrl+Shift+P) and select "Dev-Containers: Rebuild and Reopen in Container".

#### 2. xml -> yaml conversion
The configuration files have been converted from XML to YAML format for better readability and ease of use. I plan on doing the same for the CORE repo as well.

#### 3. New script directory
A new directory has been created for scripts, making it easier to manage and organize scripts related to the project. (Running, building, etc.)

#### 4. New launch configuration
There is a new launch configuration. It is intended to create more parity between the surface and core functionality. This can be found in the `ui` directory. Now to launch the surface, you can use the following command (Does not work yet, just a template):

```
ros2 launch ui surface_launch.yaml
```
> Note: Make sure to build and source your workspace before running the launch command.

After the launch command, the interface should be accessible at `http://127.0.0.1:5000`. I have run into some issues when trying to access the interface via `localhost` (which is where vscode will try to send you if you click on the link), so it is currently recommended to use the IP address directly. I have only had this issue on MacOS so far.

### Known working platforms
> Format: Device (Architecture) - OS Version (Date tested)
- M3 MacBook Pro (ARM) - MacOS Sequoia 15.0 (9/19/2024)
- Adam's Desktop (x86) - WSL2 on Windows 11  (9/20/2024)
- Xavier's Desktop (x86) - Ubuntu 22.04 LTS (9/21/2024)

### Known issues
- You cannot access any hardware yet (gamepad, etc.)

### Updates

9/19/2024: Initial commit. Implemented new .devcontainer setup, converted XML to YAML, created new script directory, and added new launch configuration. 
The only nodes that are launched with the above launch command are the 'ui' node (Flask application) and the gamepad. I have not tested with the actual hardware yet so who knows if it will work.
