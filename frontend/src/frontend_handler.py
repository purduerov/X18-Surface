from shared_msgs.msg import FinalThrustMsg
import json

def handle_frontend_event(node, event, data):


    # Check if the event is a thrust event
    if event == "frontend-sendThrusterValues":
        # Log the received message
        # node.get_logger().info(f'Received from {event} event: "{data}"')
        # JSON data is received as a string, so convert it to a dictionary

        # Check if there is already a publisher for /final_thrust
        if node.final_thrust_pub is None:
            # Create a publisher for the /final_thrust topic
            node.final_thrust_pub = node.create_publisher(FinalThrustMsg, "/final_thrust", 10)
        # Create a new message
        thrust_msg = FinalThrustMsg()

        # Make an array of the thruster values (get all values from dict)
        thrusters = list(data.values())
        # Convert to bytearray
        thrust_msg.thrusters = thrusters

        # Publish the message once
        node.final_thrust_pub.publish(thrust_msg)
        
