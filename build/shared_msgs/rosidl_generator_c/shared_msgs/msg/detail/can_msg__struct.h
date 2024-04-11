// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from shared_msgs:msg/CanMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__CAN_MSG__STRUCT_H_
#define SHARED_MSGS__MSG__DETAIL__CAN_MSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/CanMsg in the package shared_msgs.
typedef struct shared_msgs__msg__CanMsg
{
  int32_t id;
  uint64_t data;
} shared_msgs__msg__CanMsg;

// Struct for a sequence of shared_msgs__msg__CanMsg.
typedef struct shared_msgs__msg__CanMsg__Sequence
{
  shared_msgs__msg__CanMsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} shared_msgs__msg__CanMsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SHARED_MSGS__MSG__DETAIL__CAN_MSG__STRUCT_H_
