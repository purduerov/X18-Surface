// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from shared_msgs:msg/RovVelocityCommand.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__ROV_VELOCITY_COMMAND__STRUCT_H_
#define SHARED_MSGS__MSG__DETAIL__ROV_VELOCITY_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'twist'
#include "geometry_msgs/msg/detail/twist__struct.h"
// Member 'source'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/RovVelocityCommand in the package shared_msgs.
typedef struct shared_msgs__msg__RovVelocityCommand
{
  geometry_msgs__msg__Twist twist;
  rosidl_runtime_c__String source;
  bool is_fine;
  float multiplier;
  bool is_percent_power;
  bool is_pool_centric;
} shared_msgs__msg__RovVelocityCommand;

// Struct for a sequence of shared_msgs__msg__RovVelocityCommand.
typedef struct shared_msgs__msg__RovVelocityCommand__Sequence
{
  shared_msgs__msg__RovVelocityCommand * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} shared_msgs__msg__RovVelocityCommand__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SHARED_MSGS__MSG__DETAIL__ROV_VELOCITY_COMMAND__STRUCT_H_
