// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from shared_msgs:msg/FinalThrustMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__FINAL_THRUST_MSG__TRAITS_HPP_
#define SHARED_MSGS__MSG__DETAIL__FINAL_THRUST_MSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "shared_msgs/msg/detail/final_thrust_msg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace shared_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const FinalThrustMsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: thrusters
  {
    if (msg.thrusters.size() == 0) {
      out << "thrusters: []";
    } else {
      out << "thrusters: [";
      size_t pending_items = msg.thrusters.size();
      for (auto item : msg.thrusters) {
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
  const FinalThrustMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: thrusters
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.thrusters.size() == 0) {
      out << "thrusters: []\n";
    } else {
      out << "thrusters:\n";
      for (auto item : msg.thrusters) {
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

inline std::string to_yaml(const FinalThrustMsg & msg, bool use_flow_style = false)
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
  const shared_msgs::msg::FinalThrustMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  shared_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use shared_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const shared_msgs::msg::FinalThrustMsg & msg)
{
  return shared_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<shared_msgs::msg::FinalThrustMsg>()
{
  return "shared_msgs::msg::FinalThrustMsg";
}

template<>
inline const char * name<shared_msgs::msg::FinalThrustMsg>()
{
  return "shared_msgs/msg/FinalThrustMsg";
}

template<>
struct has_fixed_size<shared_msgs::msg::FinalThrustMsg>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<shared_msgs::msg::FinalThrustMsg>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<shared_msgs::msg::FinalThrustMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SHARED_MSGS__MSG__DETAIL__FINAL_THRUST_MSG__TRAITS_HPP_
