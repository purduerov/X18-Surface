// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from shared_msgs:msg/FinalThrustMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__FINAL_THRUST_MSG__STRUCT_HPP_
#define SHARED_MSGS__MSG__DETAIL__FINAL_THRUST_MSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__shared_msgs__msg__FinalThrustMsg __attribute__((deprecated))
#else
# define DEPRECATED__shared_msgs__msg__FinalThrustMsg __declspec(deprecated)
#endif

namespace shared_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct FinalThrustMsg_
{
  using Type = FinalThrustMsg_<ContainerAllocator>;

  explicit FinalThrustMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<uint8_t, 8>::iterator, uint8_t>(this->thrusters.begin(), this->thrusters.end(), 0);
    }
  }

  explicit FinalThrustMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : thrusters(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<uint8_t, 8>::iterator, uint8_t>(this->thrusters.begin(), this->thrusters.end(), 0);
    }
  }

  // field types and members
  using _thrusters_type =
    std::array<uint8_t, 8>;
  _thrusters_type thrusters;

  // setters for named parameter idiom
  Type & set__thrusters(
    const std::array<uint8_t, 8> & _arg)
  {
    this->thrusters = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    shared_msgs::msg::FinalThrustMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const shared_msgs::msg::FinalThrustMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<shared_msgs::msg::FinalThrustMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<shared_msgs::msg::FinalThrustMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      shared_msgs::msg::FinalThrustMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<shared_msgs::msg::FinalThrustMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      shared_msgs::msg::FinalThrustMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<shared_msgs::msg::FinalThrustMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<shared_msgs::msg::FinalThrustMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<shared_msgs::msg::FinalThrustMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__shared_msgs__msg__FinalThrustMsg
    std::shared_ptr<shared_msgs::msg::FinalThrustMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__shared_msgs__msg__FinalThrustMsg
    std::shared_ptr<shared_msgs::msg::FinalThrustMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FinalThrustMsg_ & other) const
  {
    if (this->thrusters != other.thrusters) {
      return false;
    }
    return true;
  }
  bool operator!=(const FinalThrustMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FinalThrustMsg_

// alias to use template instance with default allocator
using FinalThrustMsg =
  shared_msgs::msg::FinalThrustMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace shared_msgs

#endif  // SHARED_MSGS__MSG__DETAIL__FINAL_THRUST_MSG__STRUCT_HPP_
