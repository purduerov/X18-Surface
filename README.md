# <Purdue ROV X16 README>

## Table of Contents
- [About ROV](#about-rov)
- [Project Description](#project-description)
  - [System Architecture](#system-architecture)
  - [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
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

Shown below is a diagram showing the X16 system architecture. Each white box represents a ROS node controlling a part of the system. 

<div align="center">
  <i>Figure 1: X16 System Architecture</i><br>
  <img src="https://github.com/purduerov/X16-Surface/assets/115110018/0f7b27da-1e25-4b1f-817c-2d3890259eed" alt="x16_system_architecture" width="650" height="450" />
</div>

### Key Features 

- Efficient Startup: X16 is designed for the entire system to be initialized on startup, including launching the frontend, starting the ROS nodes for the frontend and backend, and connecting to the gamepad.
- Seamless Integration: X16 Surface serves to connect the full stack of software for the ROV.
- Enchanced User Interface: The user interface is built using Python Qt5, which allows for flexibility and modularity with all of the components (widgets) needed for piloting the ROV. The user interface displays four camera streams from the ROV, thruster outputs, velocity and depth sensor readouts, and tool controls. 

## Installation

To install the dependancies for the frontend, you can run the following command:
```bash 
pip install -r X16-Surface/ui/requirements.txt
```

## Usage 

## Credits

