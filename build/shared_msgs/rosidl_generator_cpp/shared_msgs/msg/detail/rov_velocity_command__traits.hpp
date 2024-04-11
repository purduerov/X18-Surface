// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from shared_msgs:msg/RovVelocityCommand.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__ROV_VELOCITY_COMMAND__TRAITS_HPP_
#define SHARED_MSGS__MSG__DETAIL__ROV_VELOCITY_COMMAND__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "shared_msgs/msg/detail/rov_velocity_command__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'twist'
#include "geometry_msgs/msg/detail/twist__traits.hpp"

namespace shared_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const RovVelocityCommand & msg,
  std::ostream & out)
{
  out << "{";
  // member: twist
  {
    out << "twist: ";
    to_flow_style_yaml(msg.twist, out);
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
    out << ", ";
  }

  // member: pitch_lock
  {
    out << "pitch_lock: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch_lock, out);
    out << ", ";
  }

  // member: depth_lock
  {
    out << "depth_lock: ";
    rosidl_generator_traits::value_to_yaml(msg.depth_lock, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RovVelocityCommand & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: twist
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "twist:\n";
    to_block_style_yaml(msg.twist, out, indentation + 2);
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

  // member: pitch_lock
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pitch_lock: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch_lock, out);
    out << "\n";
  }

  // member: depth_lock
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "depth_lock: ";
    rosidl_generator_traits::value_to_yaml(msg.depth_lock, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RovVelocityCommand & msg, bool use_flow_style = false)
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
  const shared_msgs::msg::RovVelocityCommand & msg,
  std::ostream & out, size_t indentation = 0)
{
  shared_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use shared_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const shared_msgs::msg::RovVelocityCommand & msg)
{
  return shared_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<shared_msgs::msg::RovVelocityCommand>()
{
  return "shared_msgs::msg::RovVelocityCommand";
}

template<>
inline const char * name<shared_msgs::msg::RovVelocityCommand>()
{
  return "shared_msgs/msg/RovVelocityCommand";
}

template<>
struct has_fixed_size<shared_msgs::msg::RovVelocityCommand>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Twist>::value> {};

template<>
struct has_bounded_size<shared_msgs::msg::RovVelocityCommand>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Twist>::value> {};

template<>
struct is_message<shared_msgs::msg::RovVelocityCommand>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SHARED_MSGS__MSG__DETAIL__ROV_VELOCITY_COMMAND__TRAITS_HPP_
