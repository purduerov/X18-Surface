# Scripts Directory

This directory contains utility scripts for the X17-Surface project, primarily focused on setup, building, and maintaining the ROS 2 workspace.

## Getting Started

There are two main environements the X17-Surface project is intended to run on:

- **Linux**: The primary development and deployment environment for the project.

    To run this project on linux, ensure you are runing the correct version of Ubuntu (22.04) and have the required dependencies installed. The `install.sh` script will help set up the environment.

    You can then run the `build.sh` script to build the ROS 2 workspace and the `run.sh` script to launch the project.

- **Devcontainer**: This is a Docker-based development environment that mimics the Linux setup, allowing for consistent development across different machines. Communication with X17-Core repository will not be functional in this environment, as it is not intended for deployment. It is intended more as a UI development environment.

    To run this project in a devcontainer, ensure you have Docker installed and running. You can then open the project in Visual Studio Code with the devcontainer configuration, which will automatically set up the environment.

    Once inside the devcontainer, you can run the `build.sh` script to build the ROS 2 workspace and the `run.sh` script to launch the project.

## Available Scripts

### `build.sh`

Builds the ROS 2 workspace using colcon.

#### Functionality:

- Checks for the MediaMTX executable and prompts to install if missing
- Creates/manages the .env file with required environment variables
- Sets up ROS 2 environment with domain ID 69

#### Usage:
```bash
./scripts/build.sh
```

### `clean.sh`

Cleans up build artifacts and temporary files from the workspace.

#### Functionality:
- Removes the `build` and `log` directories by default
- Optionally removes the `install` and `logs` directories and the MediaMTX executable

#### Usage:
```bash
./scripts/clean.sh [OPTION]
```

#### Options:
- -h, --help - Show help message and exit
- -p, --purge - Perform a more extensive cleanup

### `install.sh`

Sets up the ROS 2 environment and installs the required dependencies for the X17-Surface project.

> **Warning:** This script is intended to be run in a Linux environment only.

#### Functionality:
- Installs Python 3.10 and development tools
- Installs pip and required Python packages from requirements.txt
- Installs colcon for ROS 2 building
- Installs MediaMTX (by running the `install_mediatmx.sh` script)

#### Usage:
```bash
./scripts/install.sh
```

### `install_mediatmx.sh`

Installs MediaMTX, the media server used in the X17-Surface project.
Here is a link to the [MediaMTX GitHub repository](https://github.com/bluenviron/mediamtx)

This script is run automatically by `install.sh` and `build.sh` if MediaMTX is not already installed.

#### Functionality:
- Determine the system architecture (x86_64 or arm64)
- Downloads the appropriate MediaMTX binary for the system architecture
- Extracts and moves the binary to the `ros/mediamtx_node/src` directory

#### Usage:
```bash
./scripts/install_mediatmx.sh
```

### `run.sh`

Runs the ROS 2 launch file for the X17-Surface project.

#### Functionality:
- Sources the ROS 2 environment and sets the ROS domain ID to 69
- Sets up the log directory for the current date and time
- Launches the `x17_surface.launch.py` file with the specified parameters
- Tees the output to a log file in the `logs` directory

