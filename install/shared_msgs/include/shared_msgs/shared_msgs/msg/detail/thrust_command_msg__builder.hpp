// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from shared_msgs:msg/ThrustCommandMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__THRUST_COMMAND_MSG__BUILDER_HPP_
#define SHARED_MSGS__MSG__DETAIL__THRUST_COMMAND_MSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "shared_msgs/msg/detail/thrust_command_msg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace shared_msgs
{

namespace msg
{

namespace builder
{

class Init_ThrustCommandMsg_is_pool_centric
{
public:
  explicit Init_ThrustCommandMsg_is_pool_centric(::shared_msgs::msg::ThrustCommandMsg & msg)
  : msg_(msg)
  {}
  ::shared_msgs::msg::ThrustCommandMsg is_pool_centric(::shared_msgs::msg::ThrustCommandMsg::_is_pool_centric_type arg)
  {
    msg_.is_pool_centric = std::move(arg);
    return std::move(msg_);
  }

private:
  ::shared_msgs::msg::ThrustCommandMsg msg_;
};

class Init_ThrustCommandMsg_is_fine
{
public:
  explicit Init_ThrustCommandMsg_is_fine(::shared_msgs::msg::ThrustCommandMsg & msg)
  : msg_(msg)
  {}
  Init_ThrustCommandMsg_is_pool_centric is_fine(::shared_msgs::msg::ThrustCommandMsg::_is_fine_type arg)
  {
    msg_.is_fine = std::move(arg);
    return Init_ThrustCommandMsg_is_pool_centric(msg_);
  }

private:
  ::shared_msgs::msg::ThrustCommandMsg msg_;
};

class Init_ThrustCommandMsg_desired_thrust
{
public:
  Init_ThrustCommandMsg_desired_thrust()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ThrustCommandMsg_is_fine desired_thrust(::shared_msgs::msg::ThrustCommandMsg::_desired_thrust_type arg)
  {
    msg_.desired_thrust = std::move(arg);
    return Init_ThrustCommandMsg_is_fine(msg_);
  }

private:
  ::shared_msgs::msg::ThrustCommandMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::shared_msgs::msg::ThrustCommandMsg>()
{
  return shared_msgs::msg::builder::Init_ThrustCommandMsg_desired_thrust();
}

}  // namespace shared_msgs

#endif  // SHARED_MSGS__MSG__DETAIL__THRUST_COMMAND_MSG__BUILDER_HPP_
