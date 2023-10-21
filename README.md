# <Purdue ROV X16 README>
<img src="https://github.com/purduerov/X16-Surface/assets/115110018/fddcf4fb-4822-48c0-8f07-e30a6efc2f94" width="160" height="200" alt="rov_logo">

## Table of Contents
- [About ROV](#about-rov)
- [Project Description](#project-description)
  - [System Architecture](#system-architecture)
  - [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
  - [Startup](#startup)
  - [User Interface](#user-interface)
  - [Camera Streams](#camera-streams)
  - [Troubleshooting](#troubleshooting)
  - [Documentation](#documentation)
- [Credits](#credits)
- [Contact Information](#contact-information)

## About ROV 

The Remotely Operated underwater Vehicle (ROV) team was founded as a committee within Purdue IEEE Student Organization in 2008 with a small but dedicated group of five students. Today, the team's mission is to foster technical and professional skills of its members by designing, constructing, and testing an innovative underwater vehicle to compete in the MATE Center International ROV Competition.

The ROV team is comprised of both engineering and non-engineering students working collaboratively on a hands-on project from the vehicle's design and prototyping phase, to its construction and testing, and ultimately competition performance. The team fosters a multidisciplinary spirit so that the best ideas may come forth. In addition to the mission, the MATE competition also requires a professional presentation, public display poster, and technical documentation.

Because the vehicle requires excellence in design, construction, and presentation, the team members are themselves multidisciplinary collaborators and experts in their own discipline. Members learn to communicate clearly with each other and with clients while managing their own project responsibilities. Through various outreach events during the year, the team aims to inspire future generations to enter STEM (Science, Technology, Engineering, and Mathematics) fields.

For more current and past information view the links to the left or contact us as rov@purdueieee.org. The ROV team will be accepting new members at the beginning of each semester.

## Project Description 

X16 Surface contains the frontend and backend processes for the ROV. For the frontend, the surface (computer) connects the user interface with the cameras and gamepad, allowing us to display the camera steams, controls, and readouts needed to successfully pilot the ROV. For the backend, the surface sends and receives information to and from the Raspberry Pi inside of the ROV, allows us to send outputs to the thrusters and tools in order to fully operate the ROV.

### System Architecture 

Shown below is a diagram showing the X16 system architecture. Each white box represents a ROS node and each arrow represents a topic which is published and subscribed to. 

<div align="center">
  <img src="https://github.com/purduerov/X16-Surface/assets/115110018/0f7b27da-1e25-4b1f-817c-2d3890259eed" alt="x16_system_architecture" width="650" height="450" /><br>
  <i>X16 System Architecture</i>
</div>

### Dependencies

#### ROS2 (Robot Operating System 2)
- **Description:** ROS2, or Robot Operating System 2, is an open-source framework designed for developing and controlling robotic systems. It provides a comprehensive suite of libraries, tools, and middleware for communication, hardware abstraction, and real-time control.
- **Nodes:** A node is a fundamental computational unit in ROS. It is an individual process that performs a specific task.
- **Master:** The ROS Master is the centralized coordination service that helps nodes discover and communicate with each other. Nodes register with the ROS Master, which maintains a registry of all active nodes.
- **Topics:** Topics are named communication channels that allow nodes to send and receive data. Nodes can publish data to a topic or subscribe to receive data from a topic.
- **Communication:** Nodes in a ROS system communicate asynchronously. This means that they can operate independently, sending nad receiving messages at their own pace. Multiple nodes can public data to the same topic, and multiple nodes can subscribe to the same topic.

#### Python Qt5
- **Description:** Python Qt5 is a Python binding for the Qt framework. Qt is a cross-platform application development framework that provides tools and libraries for creating graphical user interfaces and other software components.
- **Widgets:** Widgets are graphical components such as buttons, labels, textboxes, etc. The can be used to create the various components of a graphical user interface.
- **Layouts:** Layouts can be used to organize and arrange widgets within your window. You can also place widgets in a dock, on the tool bar, or set a central widget.
- **Signals and Slots:** Widgets emit signals in response to user action or system events (e.g., key press, key release, etc.). These signals can be connected to slots, which are functions that get called in response to signals.

#### GStreamer 

#### OpenCV

## Installation

To see all of the dependenices used for this system, navigate to **X16-Surface > ui > requirements.txt**.

To install all of the dependancies for the frontend, you can run the following command:
```bash 
pip install -r X16-Surface/ui/requirements.txt
```

## Usage 

All of the information needed for use of the X16 ROV can be found below. 

### Startup

#### Connecting the ROV

- Plug in the deathbox, ensuring that the switch is off first.
- Connect the ROV to the deathbox via the power cable in the tether.
- Connect the ROV to the router via the ethernet cable in the tether.
- Turn on the deathbox.

#### Launching the ROS2 Network

- For the locally run nodes, the launching the frontend should launch the frontend ROS nodes
- To launch the pi nodes, run the following command:
  
  ```bash
  ros2 launch rov_launch run_rov_launch.xml
  ``` 

### User Interface

### Launch UI with Surface Nodes
ros2 run ui runner.py

### Camera Streams

To launch and receive the camera streams externally, follow these instructions:

#### Launch Streams

- Plug in the ROV and connect the ethernet cable from the tether to the router. Power on the ROV.
- Connect your computer to the ROV wifi
- In your browser, search up '10.0.0.1'. This will pull up the internet configuration setting for the router.
- In *Attatched Devices*, you can see the IP address assigned to the Raspberry Pi and the IP address assigned to your computer.
- In a terminal, ssh into the pi using the following command:
  ```bash
  ssh pi@<rov_ip_address>
  ```
- To launch the camera streams, run one of the following commands while ssh'd into the pi. You will have to change the *host* to match the IP address of your computer.
  NOTE: running a command will begin a process timer. If you want to launch and receive multiple streams you will have to ssh into multiple terminal windows.

  Stream 1 (Front-facing camera)
  ```bash
  gst-launch-1.0 -v v4l2src device=/dev/video8 ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host=10.0.0.103 port=5600 sync=false buffer-size=1048576
  ```

  Stream 2 (Downward-facing camera)
  ```bash
  gst-launch-1.0 -v v4l2src device=/dev/video4 ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host=10.0.0.103 port=5601 sync=false buffer-size=1048576
  ```

  Stream 3 (Bandicam)
  ```bash
  gst-launch-1.0 -v v4l2src device=/dev/video0 ! image/jpeg, width=1920,height=1080, framerate=30/1 ! jpegparse ! queue max-size-buffers=100 ! rtpjpegpay ! udpsink host=10.0.0.101 port=5602 sync=false buffer-size=1048576
  ```

#### Receive Streams

- To receive the camera streams, run the corresponding command in a new terminal (this terminal should not be ssh'd into the pi)
  NOTE: The port for a receiving command should match the port from the corresponding launch command.

  Stream 1 (Front-facing camera)
  ```bash
  gst-launch-1.0 udpsrc port=5600 ! application/x-rtp ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false
  ```

  Stream 2 (Downward-facing camera)
  ```bash
  gst-launch-1.0 udpsrc port=5601 ! application/x-rtp ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false
  ```

  Stream 3 (Bandicam)
  ```bash
  gst-launch-1.0 -v v4l2src device=/dev/video0 ! image/jpeg, width=1920,height=1080, framerate=30/1 ! jpegparse ! queue max-size-buffers=100 ! rtpjpegpay ! udpsink host=10.0.0.101 port=5602 sync=false buffer-size=1048576
  ```

## Using the Gamepad
  <img src="https://github.com/purduerov/X16-Surface/assets/28714773/623a7855-31f7-410b-8da2-ef688b6bcab6" alt="gamepad" width="50%" height="50%"/>
  The above image is the xbox controller used as the gamepad for the ROV. 

  The gamepad is used to control linear and angular movement of the ROV as well as the movement mode that it is in. The gamepad is also used to control the solenoids and other tools located on the ROV. 

  ### Movement
   The ROV is capable of movement in the x,y,z linear directions as well as the x,y,z angular directions also called roll, pitch, and yaw respectively. 

   Linear x: Move the left stick (LS) up for positive x movement and down for negative x movement.
   Linear y: Move the left stick (LS) left for positive y movement and right for negative y movement.
   Linear z: Hold down the right trigger (RT) for positive z movement and the left trigger (LT) for negative z movement.

   Angular x (roll): Hold down the right bumper (RB) for positive x roll and the left bumper (LB) for negative x roll.
   Angular y (pitch): Move the right stick (RS) up for positive y pitch and the right stick (RS) down for negative y pitch.
   Angular z (yaw): Move the right stick (RS) left for positive z yaw and the left stick (LS) right for positive z yaw.

   Tool 1: Press button A
   Tool 2: Press button B
   Tool 3: Press button Y
   Tool 4: Press button X
  
### Troubleshooting 

https://chat.openai.com/

### Documentation

For more documentation on using X16 Surface, visit the Purdue ROV BookStack.

## Credits

X16 Software has been a collaborative effort involving the dedication and contributions of many individuals, including:

### Project Team
- **Software Lead:** Neil Brown
- **Design and UI:** Ethan Burmane, Caden Brennan
- **Hardware Specialist:** Xavier Callait

### Special Thanks
- **Purdue IEEE:** For their ongoing support and collaboration.
- **MATE ROV:** For hosting the annual MATE ROV Competition.

## Contact Information

For any inquires about Purdue ROV, please send an email to rov@purdueieee.org

For more information on MATE ROV, visit https://materovcompetition.org/

To see updates about Purdue ROV, follow us on social media:
- **Instagram:** @purduerov
- **Linkedin:** https://www.linkedin.com/company/purdue-rov

