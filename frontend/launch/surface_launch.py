from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='frontend',
            executable='app.py',
            namespace='rov',
        ),
        Node(
            package='demo_publisher',
            executable='demo_publisher.py',
            namespace='rov',
        ),
        TimerAction(
            period=5.0,  # Delay for 30 seconds
            actions=[
                Node(
                    package='demo_subscriber',
                    executable='demo_subscriber.py',
                    namespace='rov',
                )
            ]
        ),
    ])
