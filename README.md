# <Purdue ROV X16 README>

## Table of Contents
- [About ROV](#about-rov)
- [Project Description](#project-description)
  - [System Architecture](#system-architecture)
  - [Key Features](#key-features)
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

### Key Features 

- **Efficient Startup:** X16 is designed for the entire system to be initialized on startup, including launching the frontend, starting the ROS nodes for the frontend and backend, and connecting to the gamepad.
- **Seamless Integration:** X16 Surface serves to connect the full stack of software for the ROV.
- **Enchanced User Interface:** The user interface is built using Python Qt5, which allows for flexibility and modularity with all of the components (widgets) needed for piloting the ROV. The user interface displays four camera streams from the ROV, thruster outputs, velocity and depth sensor readouts, and tool controls. 

## Installation

To see all of the dependenices used for this system, navigate to **X16-Surface > ui > requirements.txt**.

To install all of the dependancies for the frontend, you can run the following command:
```bash 
pip install -r X16-Surface/ui/requirements.txt
```

## Usage 

All of the information needed for use of the X16 ROV can be found below. 

### Startup

### User Interface

### Camera Streams

To launch and receive the camera streams externally, follow these instructions:

#### Launch Streams

- Make sure the ROV is plugged in and turned on. The ethernet cable should be plugged into the router.
- Connect to the ROV wifi
- In your browser, search up '10.0.0.1'. This will pull up the internet configuration setting for the router.
- In *Attatched Devices*, you can see the IP address for the ROV under *Wired Devices*, and you can see the IP address for your computer under *Wireless Devices*.
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
  
### Troubleshooting 

https://chat.openai.com/

### Documentation



## Credits

X16 Software has been a collaborative effort involving the dedication and contributions of many individuals, including:

### Project Team
- **Software Lead:** Neil Brown
- **Design and UI:** Ethan Burmane, Caden Brennan
- **Hardware Specialist:** Xavier Callait

## Contact Information


