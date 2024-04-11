// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from shared_msgs:msg/ToolsCommandMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__TOOLS_COMMAND_MSG__TRAITS_HPP_
#define SHARED_MSGS__MSG__DETAIL__TOOLS_COMMAND_MSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "shared_msgs/msg/detail/tools_command_msg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace shared_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const ToolsCommandMsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: tools
  {
    if (msg.tools.size() == 0) {
      out << "tools: []";
    } else {
      out << "tools: [";
      size_t pending_items = msg.tools.size();
      for (auto item : msg.tools) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: motor_tools
  {
    out << "motor_tools: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_tools, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ToolsCommandMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: tools
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.tools.size() == 0) {
      out << "tools: []\n";
    } else {
      out << "tools:\n";
      for (auto item : msg.tools) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: motor_tools
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor_tools: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_tools, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ToolsCommandMsg & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace shared_msgs

namespace rosidl_generator_traits
{

[[deprecated("use shared_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const shared_msgs::msg::ToolsCommandMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  shared_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use shared_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const shared_msgs::msg::ToolsCommandMsg & msg)
{
  return shared_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<shared_msgs::msg::ToolsCommandMsg>()
{
  return "shared_msgs::msg::ToolsCommandMsg";
}

template<>
inline const char * name<shared_msgs::msg::ToolsCommandMsg>()
{
  return "shared_msgs/msg/ToolsCommandMsg";
}

template<>
struct has_fixed_size<shared_msgs::msg::ToolsCommandMsg>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<shared_msgs::msg::ToolsCommandMsg>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<shared_msgs::msg::ToolsCommandMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SHARED_MSGS__MSG__DETAIL__TOOLS_COMMAND_MSG__TRAITS_HPP_
