// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from shared_msgs:msg/RovVelocityCommand.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__ROV_VELOCITY_COMMAND__STRUCT_HPP_
#define SHARED_MSGS__MSG__DETAIL__ROV_VELOCITY_COMMAND__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'twist'
#include "geometry_msgs/msg/detail/twist__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__shared_msgs__msg__RovVelocityCommand __attribute__((deprecated))
#else
# define DEPRECATED__shared_msgs__msg__RovVelocityCommand __declspec(deprecated)
#endif

namespace shared_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RovVelocityCommand_
{
  using Type = RovVelocityCommand_<ContainerAllocator>;

  explicit RovVelocityCommand_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : twist(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_fine = 0;
      this->is_pool_centric = false;
      this->pitch_lock = false;
      this->depth_lock = false;
    }
  }

  explicit RovVelocityCommand_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : twist(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_fine = 0;
      this->is_pool_centric = false;
      this->pitch_lock = false;
      this->depth_lock = false;
    }
  }

  // field types and members
  using _twist_type =
    geometry_msgs::msg::Twist_<ContainerAllocator>;
  _twist_type twist;
  using _is_fine_type =
    uint8_t;
  _is_fine_type is_fine;
  using _is_pool_centric_type =
    bool;
  _is_pool_centric_type is_pool_centric;
  using _pitch_lock_type =
    bool;
  _pitch_lock_type pitch_lock;
  using _depth_lock_type =
    bool;
  _depth_lock_type depth_lock;

  // setters for named parameter idiom
  Type & set__twist(
    const geometry_msgs::msg::Twist_<ContainerAllocator> & _arg)
  {
    this->twist = _arg;
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
  Type & set__pitch_lock(
    const bool & _arg)
  {
    this->pitch_lock = _arg;
    return *this;
  }
  Type & set__depth_lock(
    const bool & _arg)
  {
    this->depth_lock = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    shared_msgs::msg::RovVelocityCommand_<ContainerAllocator> *;
  using ConstRawPtr =
    const shared_msgs::msg::RovVelocityCommand_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<shared_msgs::msg::RovVelocityCommand_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<shared_msgs::msg::RovVelocityCommand_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      shared_msgs::msg::RovVelocityCommand_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<shared_msgs::msg::RovVelocityCommand_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      shared_msgs::msg::RovVelocityCommand_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<shared_msgs::msg::RovVelocityCommand_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<shared_msgs::msg::RovVelocityCommand_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<shared_msgs::msg::RovVelocityCommand_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__shared_msgs__msg__RovVelocityCommand
    std::shared_ptr<shared_msgs::msg::RovVelocityCommand_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__shared_msgs__msg__RovVelocityCommand
    std::shared_ptr<shared_msgs::msg::RovVelocityCommand_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RovVelocityCommand_ & other) const
  {
    if (this->twist != other.twist) {
      return false;
    }
    if (this->is_fine != other.is_fine) {
      return false;
    }
    if (this->is_pool_centric != other.is_pool_centric) {
      return false;
    }
    if (this->pitch_lock != other.pitch_lock) {
      return false;
    }
    if (this->depth_lock != other.depth_lock) {
      return false;
    }
    return true;
  }
  bool operator!=(const RovVelocityCommand_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RovVelocityCommand_

// alias to use template instance with default allocator
using RovVelocityCommand =
  shared_msgs::msg::RovVelocityCommand_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace shared_msgs

#endif  // SHARED_MSGS__MSG__DETAIL__ROV_VELOCITY_COMMAND__STRUCT_HPP_
