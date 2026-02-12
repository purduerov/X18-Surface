cmake_minimum_required(VERSION 3.8)
project(LaptopPhotoStream)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(cv_bridge REQUIRED)

install(PROGRAMS
  src/LapPhoto.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()

