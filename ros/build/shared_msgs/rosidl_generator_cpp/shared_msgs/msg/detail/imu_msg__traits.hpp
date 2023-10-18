// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from shared_msgs:msg/ImuMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__IMU_MSG__TRAITS_HPP_
#define SHARED_MSGS__MSG__DETAIL__IMU_MSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "shared_msgs/msg/detail/imu_msg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace shared_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const ImuMsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: gyro
  {
    if (msg.gyro.size() == 0) {
      out << "gyro: []";
    } else {
      out << "gyro: [";
      size_t pending_items = msg.gyro.size();
      for (auto item : msg.gyro) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: accel
  {
    if (msg.accel.size() == 0) {
      out << "accel: []";
    } else {
      out << "accel: [";
      size_t pending_items = msg.accel.size();
      for (auto item : msg.accel) {
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
  const ImuMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: gyro
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.gyro.size() == 0) {
      out << "gyro: []\n";
    } else {
      out << "gyro:\n";
      for (auto item : msg.gyro) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: accel
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.accel.size() == 0) {
      out << "accel: []\n";
    } else {
      out << "accel:\n";
      for (auto item : msg.accel) {
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

inline std::string to_yaml(const ImuMsg & msg, bool use_flow_style = false)
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
  const shared_msgs::msg::ImuMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  shared_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use shared_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const shared_msgs::msg::ImuMsg & msg)
{
  return shared_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<shared_msgs::msg::ImuMsg>()
{
  return "shared_msgs::msg::ImuMsg";
}

template<>
inline const char * name<shared_msgs::msg::ImuMsg>()
{
  return "shared_msgs/msg/ImuMsg";
}

template<>
struct has_fixed_size<shared_msgs::msg::ImuMsg>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<shared_msgs::msg::ImuMsg>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<shared_msgs::msg::ImuMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SHARED_MSGS__MSG__DETAIL__IMU_MSG__TRAITS_HPP_
