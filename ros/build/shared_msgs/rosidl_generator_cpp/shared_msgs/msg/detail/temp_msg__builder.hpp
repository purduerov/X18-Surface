// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from shared_msgs:msg/TempMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__TEMP_MSG__BUILDER_HPP_
#define SHARED_MSGS__MSG__DETAIL__TEMP_MSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "shared_msgs/msg/detail/temp_msg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace shared_msgs
{

namespace msg
{

namespace builder
{

class Init_TempMsg_temperature
{
public:
  Init_TempMsg_temperature()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::shared_msgs::msg::TempMsg temperature(::shared_msgs::msg::TempMsg::_temperature_type arg)
  {
    msg_.temperature = std::move(arg);
    return std::move(msg_);
  }

private:
  ::shared_msgs::msg::TempMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::shared_msgs::msg::TempMsg>()
{
  return shared_msgs::msg::builder::Init_TempMsg_temperature();
}

}  // namespace shared_msgs

#endif  // SHARED_MSGS__MSG__DETAIL__TEMP_MSG__BUILDER_HPP_
