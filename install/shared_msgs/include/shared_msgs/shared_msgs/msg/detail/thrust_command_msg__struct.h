// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from shared_msgs:msg/ThrustCommandMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__THRUST_COMMAND_MSG__STRUCT_H_
#define SHARED_MSGS__MSG__DETAIL__THRUST_COMMAND_MSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/ThrustCommandMsg in the package shared_msgs.
typedef struct shared_msgs__msg__ThrustCommandMsg
{
  float desired_thrust[6];
  uint8_t is_fine;
  bool is_pool_centric;
} shared_msgs__msg__ThrustCommandMsg;

// Struct for a sequence of shared_msgs__msg__ThrustCommandMsg.
typedef struct shared_msgs__msg__ThrustCommandMsg__Sequence
{
  shared_msgs__msg__ThrustCommandMsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} shared_msgs__msg__ThrustCommandMsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SHARED_MSGS__MSG__DETAIL__THRUST_COMMAND_MSG__STRUCT_H_
