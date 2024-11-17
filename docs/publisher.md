# Writing a Publisher node in Python

**Author: Adam Kahl**  
**Created on: [2024-11-17]**  
**Last updated: [2024-11-17]**  
**ROS Version: ROS 2 Humble**  

## Table of contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Example complete Publisher](#example-code)
- [Explanation of the code](#explanation-of-the-code)
- [Running the Publisher node](#running-the-publisher-node)
- [Troubleshooting](#troubleshooting)

## Introduction

This guide shows you how Purdue ROV writes publisher nodes in Python. Publisher nodes are used to send messages to a topic. In this example, we will write a publisher node that publishes messages to the `/count` topic.

## Prerequisites

This tutorial assumes you have followed the [ros setup instructions](/docs/ros_setup.md) or the [docker setup instructions](docs/docker_setup.md) and have a basic understanding of Python.

It also assumes you are in a properly setup ROS 2 workspace. You can learn more about the structure of the ROS 2 workspace [here]().

## Example code

Here is a template for a publisher node in Python:

```python
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher = self.create_publisher(String, 'count', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 100

    def timer_callback(self):
        msg = String()
        msg.data = str(self.count)
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.count = self.count - 1 if self.count > 0 else 100


def main():
    rclpy.init()
    publisher_node = PublisherNode()
    rclpy.spin(publisher_node)
    publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
```

## Explanation of the code

1. Shebang line:

    ```python
    #!/usr/bin/env python3
    ```

    The shebang line `#!/usr/bin/env python3` is used to specify the Python interpreter to use when running the script. You can learn more about shebang lines [here](https://en.wikipedia.org/wiki/Shebang_(Unix)).

2. Importing necessary libraries:

    ```python
    import rclpy
    from rclpy.node import Node
    from std_msgs.msg import String
    ```

    - `rclpy`: The main library for writing ROS 2 nodes in Python. It provides tools to create and manage nodes and handle the ROS 2 lifecycle.
    - `Node`: A base class for all ROS 2 nodes, providing core functionality like logging and communication.
    - `std_msgs.msg.String`: A standard ROS 2 message type for sending and receiving text messages.

3. Defining the Publisher Node

    ```python
    class PublisherNode(Node):
    ```
    - A class named `PublisherNode` is created, representing the publisher node. This name can be changed to anything you like, but it should be descriptive of the node's purpose.
    - It inherits from the `Node` class, allowing it to act as a ROS 2 node and allowing it to use the Node class's functionality, such as logging.

4. Node Initialization

    ```python
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, 'count', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 100
    ```
    - `super().__init__('publisher_node')`: Initializes the node with the name `"publisher_node"`.
    - `self.publisher`: Creates a publisher for the topic `"count"`, with message type `String` and queue size `10`.
    - `self.timer`: Creates a timer that calls the `timer_callback` function every second.
    - `self.count`: A counter that starts at `100` and decreases with each timer callback.

5. Timer Callback Function
    
    ```python
    def timer_callback(self):
        msg = String()
        msg.data = str(self.count)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.count = self.count - 1 if self.count > 0 else 100
    ```
    
    - `msg = String()`: Creates a new message object.
    - `msg.data = str(self.count)`: Sets the message content to the current counter value.
    - `self.publisher_.publish(msg)`: Publishes the message on the `"count"` topic.
    - `self.get_logger().info(...)`: Logs the published message.
    - `self.count = self.count - 1 if self.count > 0 else 100`: Decreases the counter until it reaches `0`, then resets it to `100`.

6. Main Function

    ```python
    def main():
        rclpy.init()
        publisher_node = PublisherNode()
        rclpy.spin(publisher_node)
        publisher_node.destroy_node()
        rclpy.shutdown()
    ```

    - `rclpy.init()`: Initializes the ROS 2 client library.
    - `publisher_node = PublisherNode()`: Creates an instance of the `PublisherNode` class.
    - `rclpy.spin(publisher_node)`: Enters the main event loop, waiting for callbacks to be invoked.
    - `publisher_node.destroy_node()`: Destroys the node and releases its resources.
    - `rclpy.shutdown()`: Shuts down the ROS 2 client library.

7. Script Entry Point

    ```python
    if __name__ == "__main__":
        main()
    ```

    - This ensures the script runs only if executed directly (not when imported as a module).

## Running the Publisher node

1. Source the workspace

    #### Linux (or WSL)
    ```bash
    source /opt/ros/humble/setup.bash
    ```

    #### MacOS
    ```bash
    . ~/ros2_install/ros2-osx/setup.bash
    ```

    #### Windows
    ```cmd
    call C:\dev\ros2\local_setup.bat
    ```

    You may need to adjust the path to the setup file based on your ROS 2 installation.

2. Build the workspace

    We use colcon to build the workspace. Run the following command in the root of your workspace:

    ```bash
    colcon build
    ```

3. Source the installed workspace

    ```bash
    source install/setup.bash
    ```

4. Run the publisher node

    ```bash
    ros2 run publisher_node demo_publisher.py
    ```

    Replace `publisher_node` with the name of the package containing the publisher node. 
    Replace `demo_publisher.py` with the name of the Python script containing the publisher node.

5. Verify that the publisher node is running and publishing messages.

    - You can view the active ROS nodes on your ROS network using the following command:

    ```bash
    ros2 node list
    ```

    - You can view all the topics being published on the ROS network using the following command:

    ```bash
    ros2 topic list
    ```

    - You can view the messages being published on the `/count` topic using the following command:

    ```bash
    ros2 topic echo /count
    ```

## Troubleshooting

- If you encounter any issues while running the publisher node, check the following:
    - Make sure the ROS 2 environment is properly set up.
    - Verify that the message type in the publisher matches the message type expected by any subscribers.
    - Check the topic name and ensure it matches the topic name expected by any subscribers.
    - Inspect the logs for any error messages that might indicate the cause of the issue.
    - Ensure that the ROS 2 client library is correctly initialized and shut down.
