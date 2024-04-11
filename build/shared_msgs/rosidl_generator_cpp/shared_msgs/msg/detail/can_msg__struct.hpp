// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from shared_msgs:msg/CanMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__CAN_MSG__STRUCT_HPP_
#define SHARED_MSGS__MSG__DETAIL__CAN_MSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__shared_msgs__msg__CanMsg __attribute__((deprecated))
#else
# define DEPRECATED__shared_msgs__msg__CanMsg __declspec(deprecated)
#endif

namespace shared_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct CanMsg_
{
  using Type = CanMsg_<ContainerAllocator>;

  explicit CanMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0l;
      this->data = 0ull;
    }
  }

  explicit CanMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0l;
      this->data = 0ull;
    }
  }

  // field types and members
  using _id_type =
    int32_t;
  _id_type id;
  using _data_type =
    uint64_t;
  _data_type data;

  // setters for named parameter idiom
  Type & set__id(
    const int32_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__data(
    const uint64_t & _arg)
  {
    this->data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    shared_msgs::msg::CanMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const shared_msgs::msg::CanMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<shared_msgs::msg::CanMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<shared_msgs::msg::CanMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      shared_msgs::msg::CanMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<shared_msgs::msg::CanMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      shared_msgs::msg::CanMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<shared_msgs::msg::CanMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<shared_msgs::msg::CanMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<shared_msgs::msg::CanMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__shared_msgs__msg__CanMsg
    std::shared_ptr<shared_msgs::msg::CanMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__shared_msgs__msg__CanMsg
    std::shared_ptr<shared_msgs::msg::CanMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CanMsg_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    if (this->data != other.data) {
      return false;
    }
    return true;
  }
  bool operator!=(const CanMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CanMsg_

// alias to use template instance with default allocator
using CanMsg =
  shared_msgs::msg::CanMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace shared_msgs

#endif  // SHARED_MSGS__MSG__DETAIL__CAN_MSG__STRUCT_HPP_
