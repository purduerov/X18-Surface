// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from shared_msgs:msg/FinalThrustMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__FINAL_THRUST_MSG__BUILDER_HPP_
#define SHARED_MSGS__MSG__DETAIL__FINAL_THRUST_MSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "shared_msgs/msg/detail/final_thrust_msg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace shared_msgs
{

namespace msg
{

namespace builder
{

class Init_FinalThrustMsg_thrusters
{
public:
  Init_FinalThrustMsg_thrusters()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::shared_msgs::msg::FinalThrustMsg thrusters(::shared_msgs::msg::FinalThrustMsg::_thrusters_type arg)
  {
    msg_.thrusters = std::move(arg);
    return std::move(msg_);
  }

private:
  ::shared_msgs::msg::FinalThrustMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::shared_msgs::msg::FinalThrustMsg>()
{
  return shared_msgs::msg::builder::Init_FinalThrustMsg_thrusters();
}

}  // namespace shared_msgs

#endif  // SHARED_MSGS__MSG__DETAIL__FINAL_THRUST_MSG__BUILDER_HPP_
