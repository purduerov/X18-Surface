// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from shared_msgs:msg/ToolsCommandMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__TOOLS_COMMAND_MSG__STRUCT_HPP_
#define SHARED_MSGS__MSG__DETAIL__TOOLS_COMMAND_MSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__shared_msgs__msg__ToolsCommandMsg __attribute__((deprecated))
#else
# define DEPRECATED__shared_msgs__msg__ToolsCommandMsg __declspec(deprecated)
#endif

namespace shared_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ToolsCommandMsg_
{
  using Type = ToolsCommandMsg_<ContainerAllocator>;

  explicit ToolsCommandMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<int8_t, 5>::iterator, int8_t>(this->tools.begin(), this->tools.end(), 0);
      this->motor_tools = 0;
    }
  }

  explicit ToolsCommandMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : tools(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<int8_t, 5>::iterator, int8_t>(this->tools.begin(), this->tools.end(), 0);
      this->motor_tools = 0;
    }
  }

  // field types and members
  using _tools_type =
    std::array<int8_t, 5>;
  _tools_type tools;
  using _motor_tools_type =
    uint8_t;
  _motor_tools_type motor_tools;

  // setters for named parameter idiom
  Type & set__tools(
    const std::array<int8_t, 5> & _arg)
  {
    this->tools = _arg;
    return *this;
  }
  Type & set__motor_tools(
    const uint8_t & _arg)
  {
    this->motor_tools = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    shared_msgs::msg::ToolsCommandMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const shared_msgs::msg::ToolsCommandMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<shared_msgs::msg::ToolsCommandMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<shared_msgs::msg::ToolsCommandMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      shared_msgs::msg::ToolsCommandMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<shared_msgs::msg::ToolsCommandMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      shared_msgs::msg::ToolsCommandMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<shared_msgs::msg::ToolsCommandMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<shared_msgs::msg::ToolsCommandMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<shared_msgs::msg::ToolsCommandMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__shared_msgs__msg__ToolsCommandMsg
    std::shared_ptr<shared_msgs::msg::ToolsCommandMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__shared_msgs__msg__ToolsCommandMsg
    std::shared_ptr<shared_msgs::msg::ToolsCommandMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ToolsCommandMsg_ & other) const
  {
    if (this->tools != other.tools) {
      return false;
    }
    if (this->motor_tools != other.motor_tools) {
      return false;
    }
    return true;
  }
  bool operator!=(const ToolsCommandMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ToolsCommandMsg_

// alias to use template instance with default allocator
using ToolsCommandMsg =
  shared_msgs::msg::ToolsCommandMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace shared_msgs

#endif  // SHARED_MSGS__MSG__DETAIL__TOOLS_COMMAND_MSG__STRUCT_HPP_
