#!/bin/bash

# This script is intended to install everything needed to run X17-Surface
# on a fresh install of Ubuntu 22.04 LTS

# Check if script is being run in a docker container and exit if it is
if [ -f /.dockerenv ]; then
    echo "This script cannot be run inside a Docker container."
    exit 1
fi

# Check if the script is being run as root and exit if it is not
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root."
    exit 1
fi

# Make sure the current repository is X17-Surface
if [ "$(basename "$PWD")" != "X17-Surface" ]; then
    echo "This script must be run from the X17-Surface repository."
    exit 1
fi

##### ROS INSTALLATION #####
echo "Installing ROS 2 - Humble"

# Set the locale
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

# Setup sources

# Ensure Ubuntu Universe repository is enabled
sudo apt install software-properties-common
sudo add-apt-repository universe

# Add the ROS 2 GPG key
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

# Add the repository to the sources list
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Install ROS 2 Packages
sudo apt update
sudo apt upgrade -y
sudo apt install ros-humble-desktop -y
echo "ROS 2 - Humble successfully installed"

#### INSTALL PYTHON DEPENDENCIES ####
echo "Installing Python dependencies..."

# Make sure Python 3.10 is installed
sudo apt install python3.10 python3.10-dev python3.10-venv -y

# Install pip
sudo apt -y install python3-pip

# Install python packages
sudo pip3 install -r requirements.txt
echo "Python dependencies successfully installed"

#### MEDIAMTX INSTALLATION ####
echo "Installing the most revent version of MediaMTX..."
# Function to get the latest release version from GitHub
get_latest_release() {
  curl --silent "https://api.github.com/repos/aler9/mediamtx/releases/latest" | 
  grep '"tag_name":' |                                                    
  sed -E 's/.*"([^"]+)".*/\1/'                                            
}

# Detect the system architecture
ARCH=$(uname -m)
case "$ARCH" in
  x86_64) ARCH="amd64";;
  aarch64) ARCH="arm64v8";;
  armv7l) ARCH="armv7";;
  *) echo "Unsupported architecture: $ARCH"; exit 1;;
esac

# Get the latest version
LATEST_VERSION=$(get_latest_release)

# Construct the download URL
URL="https://github.com/aler9/mediamtx/releases/download/$LATEST_VERSION/mediamtx_$LATEST_VERSION_linux_$ARCH.tar.gz"

# Download and extract the tarball
echo "Downloading $URL..."
curl -L -o mediamtx.tar.gz "$URL"

mkdir -p mediamtx
tar -xzf mediamtx.tar.gz -C mediamtx --strip-components=1

mv ./mediamtx mediamtx/mediamtx

# Cleanup
rm mediamtx.tar.gz LICENSE mediamtx.yml

echo "MediaMTX successfully installed"
