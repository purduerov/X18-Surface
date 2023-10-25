// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from shared_msgs:msg/ThrustStatusMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__THRUST_STATUS_MSG__STRUCT_H_
#define SHARED_MSGS__MSG__DETAIL__THRUST_STATUS_MSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/ThrustStatusMsg in the package shared_msgs.
typedef struct shared_msgs__msg__ThrustStatusMsg
{
  float status[8];
} shared_msgs__msg__ThrustStatusMsg;

// Struct for a sequence of shared_msgs__msg__ThrustStatusMsg.
typedef struct shared_msgs__msg__ThrustStatusMsg__Sequence
{
  shared_msgs__msg__ThrustStatusMsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} shared_msgs__msg__ThrustStatusMsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SHARED_MSGS__MSG__DETAIL__THRUST_STATUS_MSG__STRUCT_H_
