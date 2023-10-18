// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from shared_msgs:msg/CanMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__CAN_MSG__BUILDER_HPP_
#define SHARED_MSGS__MSG__DETAIL__CAN_MSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "shared_msgs/msg/detail/can_msg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace shared_msgs
{

namespace msg
{

namespace builder
{

class Init_CanMsg_data
{
public:
  explicit Init_CanMsg_data(::shared_msgs::msg::CanMsg & msg)
  : msg_(msg)
  {}
  ::shared_msgs::msg::CanMsg data(::shared_msgs::msg::CanMsg::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::shared_msgs::msg::CanMsg msg_;
};

class Init_CanMsg_id
{
public:
  Init_CanMsg_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CanMsg_data id(::shared_msgs::msg::CanMsg::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_CanMsg_data(msg_);
  }

private:
  ::shared_msgs::msg::CanMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::shared_msgs::msg::CanMsg>()
{
  return shared_msgs::msg::builder::Init_CanMsg_id();
}

}  // namespace shared_msgs

#endif  // SHARED_MSGS__MSG__DETAIL__CAN_MSG__BUILDER_HPP_
