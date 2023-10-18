// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from shared_msgs:msg/RovVelocityCommand.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__ROV_VELOCITY_COMMAND__BUILDER_HPP_
#define SHARED_MSGS__MSG__DETAIL__ROV_VELOCITY_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "shared_msgs/msg/detail/rov_velocity_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace shared_msgs
{

namespace msg
{

namespace builder
{

class Init_RovVelocityCommand_is_pool_centric
{
public:
  explicit Init_RovVelocityCommand_is_pool_centric(::shared_msgs::msg::RovVelocityCommand & msg)
  : msg_(msg)
  {}
  ::shared_msgs::msg::RovVelocityCommand is_pool_centric(::shared_msgs::msg::RovVelocityCommand::_is_pool_centric_type arg)
  {
    msg_.is_pool_centric = std::move(arg);
    return std::move(msg_);
  }

private:
  ::shared_msgs::msg::RovVelocityCommand msg_;
};

class Init_RovVelocityCommand_is_percent_power
{
public:
  explicit Init_RovVelocityCommand_is_percent_power(::shared_msgs::msg::RovVelocityCommand & msg)
  : msg_(msg)
  {}
  Init_RovVelocityCommand_is_pool_centric is_percent_power(::shared_msgs::msg::RovVelocityCommand::_is_percent_power_type arg)
  {
    msg_.is_percent_power = std::move(arg);
    return Init_RovVelocityCommand_is_pool_centric(msg_);
  }

private:
  ::shared_msgs::msg::RovVelocityCommand msg_;
};

class Init_RovVelocityCommand_multiplier
{
public:
  explicit Init_RovVelocityCommand_multiplier(::shared_msgs::msg::RovVelocityCommand & msg)
  : msg_(msg)
  {}
  Init_RovVelocityCommand_is_percent_power multiplier(::shared_msgs::msg::RovVelocityCommand::_multiplier_type arg)
  {
    msg_.multiplier = std::move(arg);
    return Init_RovVelocityCommand_is_percent_power(msg_);
  }

private:
  ::shared_msgs::msg::RovVelocityCommand msg_;
};

class Init_RovVelocityCommand_is_fine
{
public:
  explicit Init_RovVelocityCommand_is_fine(::shared_msgs::msg::RovVelocityCommand & msg)
  : msg_(msg)
  {}
  Init_RovVelocityCommand_multiplier is_fine(::shared_msgs::msg::RovVelocityCommand::_is_fine_type arg)
  {
    msg_.is_fine = std::move(arg);
    return Init_RovVelocityCommand_multiplier(msg_);
  }

private:
  ::shared_msgs::msg::RovVelocityCommand msg_;
};

class Init_RovVelocityCommand_source
{
public:
  explicit Init_RovVelocityCommand_source(::shared_msgs::msg::RovVelocityCommand & msg)
  : msg_(msg)
  {}
  Init_RovVelocityCommand_is_fine source(::shared_msgs::msg::RovVelocityCommand::_source_type arg)
  {
    msg_.source = std::move(arg);
    return Init_RovVelocityCommand_is_fine(msg_);
  }

private:
  ::shared_msgs::msg::RovVelocityCommand msg_;
};

class Init_RovVelocityCommand_twist
{
public:
  Init_RovVelocityCommand_twist()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RovVelocityCommand_source twist(::shared_msgs::msg::RovVelocityCommand::_twist_type arg)
  {
    msg_.twist = std::move(arg);
    return Init_RovVelocityCommand_source(msg_);
  }

private:
  ::shared_msgs::msg::RovVelocityCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::shared_msgs::msg::RovVelocityCommand>()
{
  return shared_msgs::msg::builder::Init_RovVelocityCommand_twist();
}

}  // namespace shared_msgs

#endif  // SHARED_MSGS__MSG__DETAIL__ROV_VELOCITY_COMMAND__BUILDER_HPP_
