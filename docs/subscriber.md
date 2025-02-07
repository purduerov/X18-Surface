# Writing a Subscriber node in Python

**Author: Adam Kahl**  
**Created on: [2024-11-17]**  
**Last updated: [2024-11-17]**  
**ROS Version: ROS 2 Humble**  

## Table of contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Example complete Subscriber](#example-code)
- [Explanation of the code](#explanation-of-the-code)
- [Running the Subscriber node](#running-the-subscriber-node)
- [Troubleshooting](#troubleshooting)

## Introduction

This guide shows you how Purdue ROV writes subscriber nodes in Python. Subscriber nodes are used to receive messages from a topic. In this example, we will write a subscriber node that listens to the `/count` topic and prints the message to the console.

## Prerequisites

This tutorial assumes you have followed the [ros setup instructions](/docs/ros_setup.md) or the [docker setup instructions](docs/docker_setup.md) and have a basic understanding of Python.

It also assumes you are in a properly setup ROS 2 workspace. You can learn more about the structure of the ROS 2 workspace [here]().

## Example complete subscriber

Here is a template for a subscriber node in Python:

```python
#!/usr/bin/env python3

# Import necessary libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# This class defines the subscriber node
class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')  # Initialize the node with a name
        
        # Subscribe to each topic in the topics dictionary
        self.create_subscription(String, 'count', self.count_callback, 10)

    # Callback function for the count topic
    def count_callback(self, msg):
        # Print the message received from the count topic
        self.get_logger().info(f'Received from count topic: "{msg.data}"')


def main():
    rclpy.init()
    subscriber_node = SubscriberNode()
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
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

3. Defining the Subscriber Node

    ```python
    class SubscriberNode(Node):
    ```
    - A class named `SubscriberNode` is created, representing the subscriber node. This name can be changed to anything you like, but it should be descriptive of the node's purpose.
    - It inherits from the `Node` class, allowing it to act as a ROS 2 node and allowing it to use the Node class's functionality, such as logging.

4. Node Initialization

    ```python
    def __init__(self):
        super().__init__('subscriber_node')  # Initialize the node with a name
    ```

    - `__init__`: This is the constructor method, called when an instance of `SubscriberNode` is created.
    - `super().__init__('subscriber_node')`: Initializes the node with the name `"subscriber_node"`, which identifies it within the ROS 2 network. Similarly, you can name your node anything you like, but it should be descriptive of the node's purpose, as well as unique within the ROS network.

5. Creating a Subscription

    ```python
    self.create_subscription(String, 'count', self.count_callback, 10)
    ```

    - Sets up a subscription to a topic named "count".
    - __Parameters__:
        1. `String`: The type of message expected on the topic (`std_msgs/String`).
        2. `'count'`: The name of the topic to subscribe to.
        3. `self.count_callback`: The callback function to handle messages from the topic.
        4. `10`: The "queue size," defining how many messages to store if they arrive faster than they are processed.

6. Callback function

    ```python
    def count_callback(self, msg):
        self.get_logger().info(f'Received from count topic: "{msg.data}"')
    ```

    - This function is called every time a new message is received on the `"count"` topic.
    - __Parameters__:
    1. `msg`: The received message, which is of type std_msgs/String.
        2. `self.get_logger().info(...)`: Logs the message contents to the console at the "info" level.
        3. `msg.data`: Accesses the text of the message.

7. Main function

    ```python
    def main():
        rclpy.init()
        subscriber_node = SubscriberNode()
        rclpy.spin(subscriber_node)
        subscriber_node.destroy_node()
        rclpy.shutdown()
    ```

    - `rclpy.init()`: Initializes the ROS 2 client library. This must be done before creating nodes.
    - `subscriber_node = SubscriberNode()`: Creates an instance of the SubscriberNode class.
    - `rclpy.spin(subscriber_node)`: Keeps the node running to listen for incoming messages. This function blocks the main thread until the node is shut down (e.g., by pressing `Ctrl+C`).
    - `subscriber_node.destroy_node()`: Cleans up resources used by the node.
    - `rclpy.shutdown()`: Shuts down the ROS 2 client library.

8. Script entry point

    ```python
    if __name__ == "__main__":
        main()
    ```

    - This ensures the script runs only if executed directly (not when imported as a module).

## Running the Subscriber node

1. Source the workspace

    #### Linux
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

4. Run the subscriber node

    ```bash
    ros2 run subscriber_node demo_subscriber.py
    ```

    Replace `subscriber_node` with the name of the package containing the subscriber node. 
    Replace `demo_subscriber.py` with the name of the Python script containing the subscriber node.

5. Verify that the subscriber node is running and receiving messages from the publisher node.

    - The subscriber node should start listening to the `/count` topic and print the messages received from the publisher node to the console.

    - You can view the active ROS nodes on your ROS nework using the following command:

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

- If you encounter any issues while running the subscriber node, check the following:
    - Make sure the ROS 2 environment is properly set up.
    - Verify that the message type in the subscriber matches the message type published by the publisher node.
    - Check the topic name and ensure it matches the topic name published by the publisher node.
    - Inspect the logs for any error messages that might indicate the cause of the issue.
    - Ensure that the ROS 2 client library is correctly initialized and shut down.