// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from shared_msgs:msg/ComMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__COM_MSG__BUILDER_HPP_
#define SHARED_MSGS__MSG__DETAIL__COM_MSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "shared_msgs/msg/detail/com_msg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace shared_msgs
{

namespace msg
{

namespace builder
{

class Init_ComMsg_com
{
public:
  Init_ComMsg_com()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::shared_msgs::msg::ComMsg com(::shared_msgs::msg::ComMsg::_com_type arg)
  {
    msg_.com = std::move(arg);
    return std::move(msg_);
  }

private:
  ::shared_msgs::msg::ComMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::shared_msgs::msg::ComMsg>()
{
  return shared_msgs::msg::builder::Init_ComMsg_com();
}

}  // namespace shared_msgs

#endif  // SHARED_MSGS__MSG__DETAIL__COM_MSG__BUILDER_HPP_
