// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from shared_msgs:msg/ToolsCommandMsg.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "shared_msgs/msg/detail/tools_command_msg__struct.hpp"
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

void ToolsCommandMsg_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) shared_msgs::msg::ToolsCommandMsg(_init);
}

void ToolsCommandMsg_fini_function(void * message_memory)
{
  auto typed_message = static_cast<shared_msgs::msg::ToolsCommandMsg *>(message_memory);
  typed_message->~ToolsCommandMsg();
}

size_t size_function__ToolsCommandMsg__tools(const void * untyped_member)
{
  (void)untyped_member;
  return 5;
}

const void * get_const_function__ToolsCommandMsg__tools(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<int8_t, 5> *>(untyped_member);
  return &member[index];
}

void * get_function__ToolsCommandMsg__tools(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<int8_t, 5> *>(untyped_member);
  return &member[index];
}

void fetch_function__ToolsCommandMsg__tools(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int8_t *>(
    get_const_function__ToolsCommandMsg__tools(untyped_member, index));
  auto & value = *reinterpret_cast<int8_t *>(untyped_value);
  value = item;
}

void assign_function__ToolsCommandMsg__tools(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int8_t *>(
    get_function__ToolsCommandMsg__tools(untyped_member, index));
  const auto & value = *reinterpret_cast<const int8_t *>(untyped_value);
  item = value;
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember ToolsCommandMsg_message_member_array[2] = {
  {
    "tools",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    5,  // array size
    false,  // is upper bound
    offsetof(shared_msgs::msg::ToolsCommandMsg, tools),  // bytes offset in struct
    nullptr,  // default value
    size_function__ToolsCommandMsg__tools,  // size() function pointer
    get_const_function__ToolsCommandMsg__tools,  // get_const(index) function pointer
    get_function__ToolsCommandMsg__tools,  // get(index) function pointer
    fetch_function__ToolsCommandMsg__tools,  // fetch(index, &value) function pointer
    assign_function__ToolsCommandMsg__tools,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "motor_tools",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(shared_msgs::msg::ToolsCommandMsg, motor_tools),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers ToolsCommandMsg_message_members = {
  "shared_msgs::msg",  // message namespace
  "ToolsCommandMsg",  // message name
  2,  // number of fields
  sizeof(shared_msgs::msg::ToolsCommandMsg),
  ToolsCommandMsg_message_member_array,  // message members
  ToolsCommandMsg_init_function,  // function to initialize message memory (memory has to be allocated)
  ToolsCommandMsg_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t ToolsCommandMsg_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &ToolsCommandMsg_message_members,
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
get_message_type_support_handle<shared_msgs::msg::ToolsCommandMsg>()
{
  return &::shared_msgs::msg::rosidl_typesupport_introspection_cpp::ToolsCommandMsg_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, shared_msgs, msg, ToolsCommandMsg)() {
  return &::shared_msgs::msg::rosidl_typesupport_introspection_cpp::ToolsCommandMsg_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
