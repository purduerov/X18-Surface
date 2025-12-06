cmake_minimum_required(VERSION 3.10)
project(heartbeat_monitor)

option(BUILD_TESTING "Enable testing" ON)
message(STATUS ">>> BUILD_TESTING = ${BUILD_TESTING}")

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)

# Python Package Installation
ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
  src/heartbeat_monitor.py
  DESTINATION lib/${PROJECT_NAME}
)

# -----------------------------
# Tests and Linting
# This section is executed ONLY if BUILD_TESTING is ON
# -----------------------------
if(BUILD_TESTING)
  # Find and include ament_cmake_pytest BEFORE calling its commands
  find_package(ament_cmake_pytest REQUIRED)
  include(ament_cmake_pytest)

  # Add the pytest tests
  ament_add_pytest_tests(
    heartbeat_monitor_tests
    test
    TIMEOUT 60
  )

  # Find and configure Linter Dependencies
  find_package(ament_lint_auto REQUIRED)

  # Skip linter checks if not using git repo or missing copyright/license
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)

  ament_lint_auto_find_test_dependencies()
endif()

# Must be the last command in the CMakeLists.txt
ament_package()
