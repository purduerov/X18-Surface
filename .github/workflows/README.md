# GitHub Workflows

This directory contains the GitHub workflows for the repository. The workflows are defined in the `.yml` files in this directory.

## Workflows

- [LINTER](./python_linter.yml): This workflow runs the linter on the Python code in the repository.
- [BUILD](./build_test.yml): This workflow builds the the ROS 2 workspace, launches the nodes and makes sure that there are no errors starting the nodes.

This workflow used to verify that all the correct nodes are running, but it seems to keep failing for some reason. Somewhere between listing the current nodes, and ckecking that all the nodes are listed, something is failing. This all occurs in the `Start and check ROS 2 nodes` step. Here is the step including the node verification:

```yaml
# Run the build script
- name: Start and check ROS 2 nodes
  run: |
    chmod +x scripts/run.sh
    scripts/run.sh &
    sleep 15  # Give nodes time to start
    export ROS_DOMAIN_ID=69
    source /opt/ros/humble/setup.bash
    source install/setup.bash
    nodes=("rov/frontend" "rov/heartbeat_monitor" "rov/mediamtx_node")
    echo "Listing ROS 2 nodes:"
    ros2 node list >> nodes.txt
    cat nodes.txt
    for node in "${nodes[@]}"; do
    if grep -q "$node" nodes.txt; then
        echo "$node is running"
    else
        echo "$node is not running"
        exit 1
    fi
    done
    # Kill ROS 2 nodes
    echo "Killing ROS 2 nodes:"
    pkill -f ros2 || true    # Success message
```