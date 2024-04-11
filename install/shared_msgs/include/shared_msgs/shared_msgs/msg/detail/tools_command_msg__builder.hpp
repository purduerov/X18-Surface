// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from shared_msgs:msg/ToolsCommandMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__TOOLS_COMMAND_MSG__BUILDER_HPP_
#define SHARED_MSGS__MSG__DETAIL__TOOLS_COMMAND_MSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "shared_msgs/msg/detail/tools_command_msg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace shared_msgs
{

namespace msg
{

namespace builder
{

class Init_ToolsCommandMsg_motor_tools
{
public:
  explicit Init_ToolsCommandMsg_motor_tools(::shared_msgs::msg::ToolsCommandMsg & msg)
  : msg_(msg)
  {}
  ::shared_msgs::msg::ToolsCommandMsg motor_tools(::shared_msgs::msg::ToolsCommandMsg::_motor_tools_type arg)
  {
    msg_.motor_tools = std::move(arg);
    return std::move(msg_);
  }

private:
  ::shared_msgs::msg::ToolsCommandMsg msg_;
};

class Init_ToolsCommandMsg_tools
{
public:
  Init_ToolsCommandMsg_tools()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ToolsCommandMsg_motor_tools tools(::shared_msgs::msg::ToolsCommandMsg::_tools_type arg)
  {
    msg_.tools = std::move(arg);
    return Init_ToolsCommandMsg_motor_tools(msg_);
  }

private:
  ::shared_msgs::msg::ToolsCommandMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::shared_msgs::msg::ToolsCommandMsg>()
{
  return shared_msgs::msg::builder::Init_ToolsCommandMsg_tools();
}

}  // namespace shared_msgs

#endif  // SHARED_MSGS__MSG__DETAIL__TOOLS_COMMAND_MSG__BUILDER_HPP_
