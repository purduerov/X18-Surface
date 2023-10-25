// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from shared_msgs:msg/ImuMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__IMU_MSG__STRUCT_H_
#define SHARED_MSGS__MSG__DETAIL__IMU_MSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/ImuMsg in the package shared_msgs.
typedef struct shared_msgs__msg__ImuMsg
{
  std_msgs__msg__Header header;
  float gyro[3];
  float accel[3];
} shared_msgs__msg__ImuMsg;

// Struct for a sequence of shared_msgs__msg__ImuMsg.
typedef struct shared_msgs__msg__ImuMsg__Sequence
{
  shared_msgs__msg__ImuMsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} shared_msgs__msg__ImuMsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SHARED_MSGS__MSG__DETAIL__IMU_MSG__STRUCT_H_
