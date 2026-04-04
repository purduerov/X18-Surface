# Check if go2rtc executable exists in /ros/go2rtc
if [ ! -f ./ros/go2rtc_node/src/go2rtc ]; then
    # Determine architecture
    # If arch is amd64 (x86_64), download the amd64 version
    # If arch is arm64 (aarch64), download the arm64 version

    # 1. Download the tar.gz file
    echo "Downloading go2rtc..."
    arch=$(uname -m)
    if [ "$arch" == "x86_64" ]; then
        echo "Architecture: amd64"
        wget -O ./ros/go2rtc_node/src/go2rtc https://github.com/AlexxIT/go2rtc/releases/download/v1.9.14/go2rtc_linux_amd64

    elif [ "$arch" == "aarch64" ]; then
        echo "Architecture: arm64"
        wget -O ./ros/go2rtc_node/src/go2rtc https://github.com/AlexxIT/go2rtc/releases/download/v1.9.14/go2rtc_linux_arm64
    else
        echo "Unsupported architecture: $arch"
        exit 1
    fi

    echo "Done!"
else
    echo "go2rtc executable found in ./ros/go2rtc_node/src"
fi
