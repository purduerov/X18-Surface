// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from shared_msgs:msg/FinalThrustMsg.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "shared_msgs/msg/detail/final_thrust_msg__rosidl_typesupport_introspection_c.h"
#include "shared_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "shared_msgs/msg/detail/final_thrust_msg__functions.h"
#include "shared_msgs/msg/detail/final_thrust_msg__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__FinalThrustMsg_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  shared_msgs__msg__FinalThrustMsg__init(message_memory);
}

void shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__FinalThrustMsg_fini_function(void * message_memory)
{
  shared_msgs__msg__FinalThrustMsg__fini(message_memory);
}

size_t shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__size_function__FinalThrustMsg__thrusters(
  const void * untyped_member)
{
  (void)untyped_member;
  return 8;
}

const void * shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__get_const_function__FinalThrustMsg__thrusters(
  const void * untyped_member, size_t index)
{
  const uint8_t * member =
    (const uint8_t *)(untyped_member);
  return &member[index];
}

void * shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__get_function__FinalThrustMsg__thrusters(
  void * untyped_member, size_t index)
{
  uint8_t * member =
    (uint8_t *)(untyped_member);
  return &member[index];
}

void shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__fetch_function__FinalThrustMsg__thrusters(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const uint8_t * item =
    ((const uint8_t *)
    shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__get_const_function__FinalThrustMsg__thrusters(untyped_member, index));
  uint8_t * value =
    (uint8_t *)(untyped_value);
  *value = *item;
}

void shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__assign_function__FinalThrustMsg__thrusters(
  void * untyped_member, size_t index, const void * untyped_value)
{
  uint8_t * item =
    ((uint8_t *)
    shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__get_function__FinalThrustMsg__thrusters(untyped_member, index));
  const uint8_t * value =
    (const uint8_t *)(untyped_value);
  *item = *value;
}

static rosidl_typesupport_introspection_c__MessageMember shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__FinalThrustMsg_message_member_array[1] = {
  {
    "thrusters",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    8,  // array size
    false,  // is upper bound
    offsetof(shared_msgs__msg__FinalThrustMsg, thrusters),  // bytes offset in struct
    NULL,  // default value
    shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__size_function__FinalThrustMsg__thrusters,  // size() function pointer
    shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__get_const_function__FinalThrustMsg__thrusters,  // get_const(index) function pointer
    shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__get_function__FinalThrustMsg__thrusters,  // get(index) function pointer
    shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__fetch_function__FinalThrustMsg__thrusters,  // fetch(index, &value) function pointer
    shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__assign_function__FinalThrustMsg__thrusters,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__FinalThrustMsg_message_members = {
  "shared_msgs__msg",  // message namespace
  "FinalThrustMsg",  // message name
  1,  // number of fields
  sizeof(shared_msgs__msg__FinalThrustMsg),
  shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__FinalThrustMsg_message_member_array,  // message members
  shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__FinalThrustMsg_init_function,  // function to initialize message memory (memory has to be allocated)
  shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__FinalThrustMsg_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__FinalThrustMsg_message_type_support_handle = {
  0,
  &shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__FinalThrustMsg_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_shared_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, shared_msgs, msg, FinalThrustMsg)() {
  if (!shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__FinalThrustMsg_message_type_support_handle.typesupport_identifier) {
    shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__FinalThrustMsg_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &shared_msgs__msg__FinalThrustMsg__rosidl_typesupport_introspection_c__FinalThrustMsg_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
