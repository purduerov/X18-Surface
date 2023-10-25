// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from shared_msgs:msg/ImuMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__IMU_MSG__STRUCT_HPP_
#define SHARED_MSGS__MSG__DETAIL__IMU_MSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__shared_msgs__msg__ImuMsg __attribute__((deprecated))
#else
# define DEPRECATED__shared_msgs__msg__ImuMsg __declspec(deprecated)
#endif

namespace shared_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ImuMsg_
{
  using Type = ImuMsg_<ContainerAllocator>;

  explicit ImuMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<float, 3>::iterator, float>(this->gyro.begin(), this->gyro.end(), 0.0f);
      std::fill<typename std::array<float, 3>::iterator, float>(this->accel.begin(), this->accel.end(), 0.0f);
    }
  }

  explicit ImuMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    gyro(_alloc),
    accel(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<float, 3>::iterator, float>(this->gyro.begin(), this->gyro.end(), 0.0f);
      std::fill<typename std::array<float, 3>::iterator, float>(this->accel.begin(), this->accel.end(), 0.0f);
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _gyro_type =
    std::array<float, 3>;
  _gyro_type gyro;
  using _accel_type =
    std::array<float, 3>;
  _accel_type accel;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__gyro(
    const std::array<float, 3> & _arg)
  {
    this->gyro = _arg;
    return *this;
  }
  Type & set__accel(
    const std::array<float, 3> & _arg)
  {
    this->accel = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    shared_msgs::msg::ImuMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const shared_msgs::msg::ImuMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<shared_msgs::msg::ImuMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<shared_msgs::msg::ImuMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      shared_msgs::msg::ImuMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<shared_msgs::msg::ImuMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      shared_msgs::msg::ImuMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<shared_msgs::msg::ImuMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<shared_msgs::msg::ImuMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<shared_msgs::msg::ImuMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__shared_msgs__msg__ImuMsg
    std::shared_ptr<shared_msgs::msg::ImuMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__shared_msgs__msg__ImuMsg
    std::shared_ptr<shared_msgs::msg::ImuMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ImuMsg_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->gyro != other.gyro) {
      return false;
    }
    if (this->accel != other.accel) {
      return false;
    }
    return true;
  }
  bool operator!=(const ImuMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ImuMsg_

// alias to use template instance with default allocator
using ImuMsg =
  shared_msgs::msg::ImuMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace shared_msgs

#endif  // SHARED_MSGS__MSG__DETAIL__IMU_MSG__STRUCT_HPP_
