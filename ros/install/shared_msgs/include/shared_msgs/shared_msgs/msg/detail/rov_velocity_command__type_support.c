// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from shared_msgs:msg/RovVelocityCommand.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "shared_msgs/msg/detail/rov_velocity_command__rosidl_typesupport_introspection_c.h"
#include "shared_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "shared_msgs/msg/detail/rov_velocity_command__functions.h"
#include "shared_msgs/msg/detail/rov_velocity_command__struct.h"


// Include directives for member types
// Member `twist`
#include "geometry_msgs/msg/twist.h"
// Member `twist`
#include "geometry_msgs/msg/detail/twist__rosidl_typesupport_introspection_c.h"
// Member `source`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void shared_msgs__msg__RovVelocityCommand__rosidl_typesupport_introspection_c__RovVelocityCommand_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  shared_msgs__msg__RovVelocityCommand__init(message_memory);
}

void shared_msgs__msg__RovVelocityCommand__rosidl_typesupport_introspection_c__RovVelocityCommand_fini_function(void * message_memory)
{
  shared_msgs__msg__RovVelocityCommand__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember shared_msgs__msg__RovVelocityCommand__rosidl_typesupport_introspection_c__RovVelocityCommand_message_member_array[6] = {
  {
    "twist",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(shared_msgs__msg__RovVelocityCommand, twist),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "source",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(shared_msgs__msg__RovVelocityCommand, source),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "is_fine",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(shared_msgs__msg__RovVelocityCommand, is_fine),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "multiplier",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(shared_msgs__msg__RovVelocityCommand, multiplier),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "is_percent_power",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(shared_msgs__msg__RovVelocityCommand, is_percent_power),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "is_pool_centric",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(shared_msgs__msg__RovVelocityCommand, is_pool_centric),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers shared_msgs__msg__RovVelocityCommand__rosidl_typesupport_introspection_c__RovVelocityCommand_message_members = {
  "shared_msgs__msg",  // message namespace
  "RovVelocityCommand",  // message name
  6,  // number of fields
  sizeof(shared_msgs__msg__RovVelocityCommand),
  shared_msgs__msg__RovVelocityCommand__rosidl_typesupport_introspection_c__RovVelocityCommand_message_member_array,  // message members
  shared_msgs__msg__RovVelocityCommand__rosidl_typesupport_introspection_c__RovVelocityCommand_init_function,  // function to initialize message memory (memory has to be allocated)
  shared_msgs__msg__RovVelocityCommand__rosidl_typesupport_introspection_c__RovVelocityCommand_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t shared_msgs__msg__RovVelocityCommand__rosidl_typesupport_introspection_c__RovVelocityCommand_message_type_support_handle = {
  0,
  &shared_msgs__msg__RovVelocityCommand__rosidl_typesupport_introspection_c__RovVelocityCommand_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_shared_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, shared_msgs, msg, RovVelocityCommand)() {
  shared_msgs__msg__RovVelocityCommand__rosidl_typesupport_introspection_c__RovVelocityCommand_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Twist)();
  if (!shared_msgs__msg__RovVelocityCommand__rosidl_typesupport_introspection_c__RovVelocityCommand_message_type_support_handle.typesupport_identifier) {
    shared_msgs__msg__RovVelocityCommand__rosidl_typesupport_introspection_c__RovVelocityCommand_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &shared_msgs__msg__RovVelocityCommand__rosidl_typesupport_introspection_c__RovVelocityCommand_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
