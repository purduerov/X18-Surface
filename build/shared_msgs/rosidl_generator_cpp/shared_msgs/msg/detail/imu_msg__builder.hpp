// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from shared_msgs:msg/ImuMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__IMU_MSG__BUILDER_HPP_
#define SHARED_MSGS__MSG__DETAIL__IMU_MSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "shared_msgs/msg/detail/imu_msg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace shared_msgs
{

namespace msg
{

namespace builder
{

class Init_ImuMsg_accel
{
public:
  explicit Init_ImuMsg_accel(::shared_msgs::msg::ImuMsg & msg)
  : msg_(msg)
  {}
  ::shared_msgs::msg::ImuMsg accel(::shared_msgs::msg::ImuMsg::_accel_type arg)
  {
    msg_.accel = std::move(arg);
    return std::move(msg_);
  }

private:
  ::shared_msgs::msg::ImuMsg msg_;
};

class Init_ImuMsg_gyro
{
public:
  explicit Init_ImuMsg_gyro(::shared_msgs::msg::ImuMsg & msg)
  : msg_(msg)
  {}
  Init_ImuMsg_accel gyro(::shared_msgs::msg::ImuMsg::_gyro_type arg)
  {
    msg_.gyro = std::move(arg);
    return Init_ImuMsg_accel(msg_);
  }

private:
  ::shared_msgs::msg::ImuMsg msg_;
};

class Init_ImuMsg_header
{
public:
  Init_ImuMsg_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ImuMsg_gyro header(::shared_msgs::msg::ImuMsg::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_ImuMsg_gyro(msg_);
  }

private:
  ::shared_msgs::msg::ImuMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::shared_msgs::msg::ImuMsg>()
{
  return shared_msgs::msg::builder::Init_ImuMsg_header();
}

}  // namespace shared_msgs

#endif  // SHARED_MSGS__MSG__DETAIL__IMU_MSG__BUILDER_HPP_
