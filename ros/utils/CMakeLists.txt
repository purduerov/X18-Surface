cmake_minimum_required(VERSION 3.5)
project(utils)

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)

ament_python_install_package(${PROJECT_NAME})

install(
  PROGRAMS
    utils/heartbeat_helper.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()