// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from shared_msgs:msg/ThrustCommandMsg.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "shared_msgs/msg/detail/thrust_command_msg__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace shared_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void ThrustCommandMsg_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) shared_msgs::msg::ThrustCommandMsg(_init);
}

void ThrustCommandMsg_fini_function(void * message_memory)
{
  auto typed_message = static_cast<shared_msgs::msg::ThrustCommandMsg *>(message_memory);
  typed_message->~ThrustCommandMsg();
}

size_t size_function__ThrustCommandMsg__desired_thrust(const void * untyped_member)
{
  (void)untyped_member;
  return 6;
}

const void * get_const_function__ThrustCommandMsg__desired_thrust(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<float, 6> *>(untyped_member);
  return &member[index];
}

void * get_function__ThrustCommandMsg__desired_thrust(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<float, 6> *>(untyped_member);
  return &member[index];
}

void fetch_function__ThrustCommandMsg__desired_thrust(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__ThrustCommandMsg__desired_thrust(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__ThrustCommandMsg__desired_thrust(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__ThrustCommandMsg__desired_thrust(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember ThrustCommandMsg_message_member_array[3] = {
  {
    "desired_thrust",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    6,  // array size
    false,  // is upper bound
    offsetof(shared_msgs::msg::ThrustCommandMsg, desired_thrust),  // bytes offset in struct
    nullptr,  // default value
    size_function__ThrustCommandMsg__desired_thrust,  // size() function pointer
    get_const_function__ThrustCommandMsg__desired_thrust,  // get_const(index) function pointer
    get_function__ThrustCommandMsg__desired_thrust,  // get(index) function pointer
    fetch_function__ThrustCommandMsg__desired_thrust,  // fetch(index, &value) function pointer
    assign_function__ThrustCommandMsg__desired_thrust,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "is_fine",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(shared_msgs::msg::ThrustCommandMsg, is_fine),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "is_pool_centric",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(shared_msgs::msg::ThrustCommandMsg, is_pool_centric),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers ThrustCommandMsg_message_members = {
  "shared_msgs::msg",  // message namespace
  "ThrustCommandMsg",  // message name
  3,  // number of fields
  sizeof(shared_msgs::msg::ThrustCommandMsg),
  ThrustCommandMsg_message_member_array,  // message members
  ThrustCommandMsg_init_function,  // function to initialize message memory (memory has to be allocated)
  ThrustCommandMsg_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t ThrustCommandMsg_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &ThrustCommandMsg_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace shared_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<shared_msgs::msg::ThrustCommandMsg>()
{
  return &::shared_msgs::msg::rosidl_typesupport_introspection_cpp::ThrustCommandMsg_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, shared_msgs, msg, ThrustCommandMsg)() {
  return &::shared_msgs::msg::rosidl_typesupport_introspection_cpp::ThrustCommandMsg_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
