// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from shared_msgs:msg/ToolsCommandMsg.idl
// generated code does not contain a copyright notice
#include "shared_msgs/msg/detail/tools_command_msg__rosidl_typesupport_fastrtps_cpp.hpp"
#include "shared_msgs/msg/detail/tools_command_msg__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace shared_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_shared_msgs
cdr_serialize(
  const shared_msgs::msg::ToolsCommandMsg & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: tools
  {
    cdr << ros_message.tools;
  }
  // Member: motor_tools
  cdr << ros_message.motor_tools;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_shared_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  shared_msgs::msg::ToolsCommandMsg & ros_message)
{
  // Member: tools
  {
    cdr >> ros_message.tools;
  }

  // Member: motor_tools
  cdr >> ros_message.motor_tools;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_shared_msgs
get_serialized_size(
  const shared_msgs::msg::ToolsCommandMsg & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: tools
  {
    size_t array_size = 5;
    size_t item_size = sizeof(ros_message.tools[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: motor_tools
  {
    size_t item_size = sizeof(ros_message.motor_tools);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_shared_msgs
max_serialized_size_ToolsCommandMsg(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: tools
  {
    size_t array_size = 5;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: motor_tools
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = shared_msgs::msg::ToolsCommandMsg;
    is_plain =
      (
      offsetof(DataType, motor_tools) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _ToolsCommandMsg__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const shared_msgs::msg::ToolsCommandMsg *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _ToolsCommandMsg__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<shared_msgs::msg::ToolsCommandMsg *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _ToolsCommandMsg__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const shared_msgs::msg::ToolsCommandMsg *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _ToolsCommandMsg__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ToolsCommandMsg(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _ToolsCommandMsg__callbacks = {
  "shared_msgs::msg",
  "ToolsCommandMsg",
  _ToolsCommandMsg__cdr_serialize,
  _ToolsCommandMsg__cdr_deserialize,
  _ToolsCommandMsg__get_serialized_size,
  _ToolsCommandMsg__max_serialized_size
};

static rosidl_message_type_support_t _ToolsCommandMsg__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_ToolsCommandMsg__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace shared_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_shared_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<shared_msgs::msg::ToolsCommandMsg>()
{
  return &shared_msgs::msg::typesupport_fastrtps_cpp::_ToolsCommandMsg__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, shared_msgs, msg, ToolsCommandMsg)() {
  return &shared_msgs::msg::typesupport_fastrtps_cpp::_ToolsCommandMsg__handle;
}

#ifdef __cplusplus
}
#endif
