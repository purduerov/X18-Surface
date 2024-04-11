// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from shared_msgs:msg/ThrustCommandMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__THRUST_COMMAND_MSG__STRUCT_HPP_
#define SHARED_MSGS__MSG__DETAIL__THRUST_COMMAND_MSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__shared_msgs__msg__ThrustCommandMsg __attribute__((deprecated))
#else
# define DEPRECATED__shared_msgs__msg__ThrustCommandMsg __declspec(deprecated)
#endif

namespace shared_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ThrustCommandMsg_
{
  using Type = ThrustCommandMsg_<ContainerAllocator>;

  explicit ThrustCommandMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<float, 6>::iterator, float>(this->desired_thrust.begin(), this->desired_thrust.end(), 0.0f);
      this->is_fine = 0;
      this->is_pool_centric = false;
    }
  }

  explicit ThrustCommandMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : desired_thrust(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<float, 6>::iterator, float>(this->desired_thrust.begin(), this->desired_thrust.end(), 0.0f);
      this->is_fine = 0;
      this->is_pool_centric = false;
    }
  }

  // field types and members
  using _desired_thrust_type =
    std::array<float, 6>;
  _desired_thrust_type desired_thrust;
  using _is_fine_type =
    uint8_t;
  _is_fine_type is_fine;
  using _is_pool_centric_type =
    bool;
  _is_pool_centric_type is_pool_centric;

  // setters for named parameter idiom
  Type & set__desired_thrust(
    const std::array<float, 6> & _arg)
  {
    this->desired_thrust = _arg;
    return *this;
  }
  Type & set__is_fine(
    const uint8_t & _arg)
  {
    this->is_fine = _arg;
    return *this;
  }
  Type & set__is_pool_centric(
    const bool & _arg)
  {
    this->is_pool_centric = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    shared_msgs::msg::ThrustCommandMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const shared_msgs::msg::ThrustCommandMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<shared_msgs::msg::ThrustCommandMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<shared_msgs::msg::ThrustCommandMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      shared_msgs::msg::ThrustCommandMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<shared_msgs::msg::ThrustCommandMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      shared_msgs::msg::ThrustCommandMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<shared_msgs::msg::ThrustCommandMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<shared_msgs::msg::ThrustCommandMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<shared_msgs::msg::ThrustCommandMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__shared_msgs__msg__ThrustCommandMsg
    std::shared_ptr<shared_msgs::msg::ThrustCommandMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__shared_msgs__msg__ThrustCommandMsg
    std::shared_ptr<shared_msgs::msg::ThrustCommandMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ThrustCommandMsg_ & other) const
  {
    if (this->desired_thrust != other.desired_thrust) {
      return false;
    }
    if (this->is_fine != other.is_fine) {
      return false;
    }
    if (this->is_pool_centric != other.is_pool_centric) {
      return false;
    }
    return true;
  }
  bool operator!=(const ThrustCommandMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ThrustCommandMsg_

// alias to use template instance with default allocator
using ThrustCommandMsg =
  shared_msgs::msg::ThrustCommandMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace shared_msgs

#endif  // SHARED_MSGS__MSG__DETAIL__THRUST_COMMAND_MSG__STRUCT_HPP_
