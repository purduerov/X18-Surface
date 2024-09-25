# Changes for X17-Surface so far on this branch

This is the phoenix branch for X17-Surface.

It is a rewrite of the previous X17-Surface codebase, with a focus on readability, maintainability, and performance.

## New structure

##### 1. New .devcontainer setup
This will allow for easier development in a consistent environment.
Requires the following components to be installed on your machine:
- Docker
- Docker Desktop
- Visual Studio Code
- Visual Studio Code Dev Containers extension

When all of the above are installed, you can open the project in Visual Studio Code and it will prompt you to reopen in a container. If you are not prompted, you can use the command palette (Ctrl+Shift+P) and select "Dev-Containers: Rebuild and Reopen in Container".

##### 2. xml -> yaml conversion
The configuration files have been converted from XML to YAML format for better readability and ease of use.

##### 3. New script directory
A new directory has been created for scripts, making it easier to manage and organize scripts related to the project.

##### 4. New launch configuration
There is a new launch configuration. It is intended to create more parity between the surface and core functionality. This can be found in the `ui` directory. Now to launch the surface, you can use the following command (Does not work yet, just a template):

```
ros2 launch ui surface_launch.yaml
```
> Note: Make sure to build and source your workspace before running the launch command.
