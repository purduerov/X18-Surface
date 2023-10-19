// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from shared_msgs:msg/ComMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__COM_MSG__TRAITS_HPP_
#define SHARED_MSGS__MSG__DETAIL__COM_MSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "shared_msgs/msg/detail/com_msg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace shared_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const ComMsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: com
  {
    if (msg.com.size() == 0) {
      out << "com: []";
    } else {
      out << "com: [";
      size_t pending_items = msg.com.size();
      for (auto item : msg.com) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ComMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: com
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.com.size() == 0) {
      out << "com: []\n";
    } else {
      out << "com:\n";
      for (auto item : msg.com) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ComMsg & msg, bool use_flow_style = false)
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
  const shared_msgs::msg::ComMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  shared_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use shared_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const shared_msgs::msg::ComMsg & msg)
{
  return shared_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<shared_msgs::msg::ComMsg>()
{
  return "shared_msgs::msg::ComMsg";
}

template<>
inline const char * name<shared_msgs::msg::ComMsg>()
{
  return "shared_msgs/msg/ComMsg";
}

template<>
struct has_fixed_size<shared_msgs::msg::ComMsg>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<shared_msgs::msg::ComMsg>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<shared_msgs::msg::ComMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SHARED_MSGS__MSG__DETAIL__COM_MSG__TRAITS_HPP_
