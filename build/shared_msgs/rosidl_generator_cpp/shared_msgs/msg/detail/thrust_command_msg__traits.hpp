// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from shared_msgs:msg/ThrustCommandMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__THRUST_COMMAND_MSG__TRAITS_HPP_
#define SHARED_MSGS__MSG__DETAIL__THRUST_COMMAND_MSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "shared_msgs/msg/detail/thrust_command_msg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace shared_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const ThrustCommandMsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: desired_thrust
  {
    if (msg.desired_thrust.size() == 0) {
      out << "desired_thrust: []";
    } else {
      out << "desired_thrust: [";
      size_t pending_items = msg.desired_thrust.size();
      for (auto item : msg.desired_thrust) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: is_fine
  {
    out << "is_fine: ";
    rosidl_generator_traits::value_to_yaml(msg.is_fine, out);
    out << ", ";
  }

  // member: is_pool_centric
  {
    out << "is_pool_centric: ";
    rosidl_generator_traits::value_to_yaml(msg.is_pool_centric, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ThrustCommandMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: desired_thrust
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.desired_thrust.size() == 0) {
      out << "desired_thrust: []\n";
    } else {
      out << "desired_thrust:\n";
      for (auto item : msg.desired_thrust) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: is_fine
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_fine: ";
    rosidl_generator_traits::value_to_yaml(msg.is_fine, out);
    out << "\n";
  }

  // member: is_pool_centric
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_pool_centric: ";
    rosidl_generator_traits::value_to_yaml(msg.is_pool_centric, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ThrustCommandMsg & msg, bool use_flow_style = false)
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
  const shared_msgs::msg::ThrustCommandMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  shared_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use shared_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const shared_msgs::msg::ThrustCommandMsg & msg)
{
  return shared_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<shared_msgs::msg::ThrustCommandMsg>()
{
  return "shared_msgs::msg::ThrustCommandMsg";
}

template<>
inline const char * name<shared_msgs::msg::ThrustCommandMsg>()
{
  return "shared_msgs/msg/ThrustCommandMsg";
}

template<>
struct has_fixed_size<shared_msgs::msg::ThrustCommandMsg>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<shared_msgs::msg::ThrustCommandMsg>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<shared_msgs::msg::ThrustCommandMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SHARED_MSGS__MSG__DETAIL__THRUST_COMMAND_MSG__TRAITS_HPP_
