// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from shared_msgs:msg/ComMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__COM_MSG__STRUCT_HPP_
#define SHARED_MSGS__MSG__DETAIL__COM_MSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__shared_msgs__msg__ComMsg __attribute__((deprecated))
#else
# define DEPRECATED__shared_msgs__msg__ComMsg __declspec(deprecated)
#endif

namespace shared_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ComMsg_
{
  using Type = ComMsg_<ContainerAllocator>;

  explicit ComMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<float, 3>::iterator, float>(this->com.begin(), this->com.end(), 0.0f);
    }
  }

  explicit ComMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : com(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<float, 3>::iterator, float>(this->com.begin(), this->com.end(), 0.0f);
    }
  }

  // field types and members
  using _com_type =
    std::array<float, 3>;
  _com_type com;

  // setters for named parameter idiom
  Type & set__com(
    const std::array<float, 3> & _arg)
  {
    this->com = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    shared_msgs::msg::ComMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const shared_msgs::msg::ComMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<shared_msgs::msg::ComMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<shared_msgs::msg::ComMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      shared_msgs::msg::ComMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<shared_msgs::msg::ComMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      shared_msgs::msg::ComMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<shared_msgs::msg::ComMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<shared_msgs::msg::ComMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<shared_msgs::msg::ComMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__shared_msgs__msg__ComMsg
    std::shared_ptr<shared_msgs::msg::ComMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__shared_msgs__msg__ComMsg
    std::shared_ptr<shared_msgs::msg::ComMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ComMsg_ & other) const
  {
    if (this->com != other.com) {
      return false;
    }
    return true;
  }
  bool operator!=(const ComMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ComMsg_

// alias to use template instance with default allocator
using ComMsg =
  shared_msgs::msg::ComMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace shared_msgs

#endif  // SHARED_MSGS__MSG__DETAIL__COM_MSG__STRUCT_HPP_
