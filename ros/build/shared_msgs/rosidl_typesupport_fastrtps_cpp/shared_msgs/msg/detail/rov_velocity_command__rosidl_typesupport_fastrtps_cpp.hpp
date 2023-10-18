// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from shared_msgs:msg/RovVelocityCommand.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__ROV_VELOCITY_COMMAND__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define SHARED_MSGS__MSG__DETAIL__ROV_VELOCITY_COMMAND__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "shared_msgs/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "shared_msgs/msg/detail/rov_velocity_command__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace shared_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_shared_msgs
cdr_serialize(
  const shared_msgs::msg::RovVelocityCommand & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_shared_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  shared_msgs::msg::RovVelocityCommand & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_shared_msgs
get_serialized_size(
  const shared_msgs::msg::RovVelocityCommand & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_shared_msgs
max_serialized_size_RovVelocityCommand(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace shared_msgs

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_shared_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, shared_msgs, msg, RovVelocityCommand)();

#ifdef __cplusplus
}
#endif

#endif  // SHARED_MSGS__MSG__DETAIL__ROV_VELOCITY_COMMAND__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
