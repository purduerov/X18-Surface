// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from shared_msgs:msg/ComMsg.idl
// generated code does not contain a copyright notice

#ifndef SHARED_MSGS__MSG__DETAIL__COM_MSG__FUNCTIONS_H_
#define SHARED_MSGS__MSG__DETAIL__COM_MSG__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "shared_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "shared_msgs/msg/detail/com_msg__struct.h"

/// Initialize msg/ComMsg message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * shared_msgs__msg__ComMsg
 * )) before or use
 * shared_msgs__msg__ComMsg__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_shared_msgs
bool
shared_msgs__msg__ComMsg__init(shared_msgs__msg__ComMsg * msg);

/// Finalize msg/ComMsg message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_shared_msgs
void
shared_msgs__msg__ComMsg__fini(shared_msgs__msg__ComMsg * msg);

/// Create msg/ComMsg message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * shared_msgs__msg__ComMsg__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_shared_msgs
shared_msgs__msg__ComMsg *
shared_msgs__msg__ComMsg__create();

/// Destroy msg/ComMsg message.
/**
 * It calls
 * shared_msgs__msg__ComMsg__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_shared_msgs
void
shared_msgs__msg__ComMsg__destroy(shared_msgs__msg__ComMsg * msg);

/// Check for msg/ComMsg message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_shared_msgs
bool
shared_msgs__msg__ComMsg__are_equal(const shared_msgs__msg__ComMsg * lhs, const shared_msgs__msg__ComMsg * rhs);

/// Copy a msg/ComMsg message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_shared_msgs
bool
shared_msgs__msg__ComMsg__copy(
  const shared_msgs__msg__ComMsg * input,
  shared_msgs__msg__ComMsg * output);

/// Initialize array of msg/ComMsg messages.
/**
 * It allocates the memory for the number of elements and calls
 * shared_msgs__msg__ComMsg__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_shared_msgs
bool
shared_msgs__msg__ComMsg__Sequence__init(shared_msgs__msg__ComMsg__Sequence * array, size_t size);

/// Finalize array of msg/ComMsg messages.
/**
 * It calls
 * shared_msgs__msg__ComMsg__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_shared_msgs
void
shared_msgs__msg__ComMsg__Sequence__fini(shared_msgs__msg__ComMsg__Sequence * array);

/// Create array of msg/ComMsg messages.
/**
 * It allocates the memory for the array and calls
 * shared_msgs__msg__ComMsg__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_shared_msgs
shared_msgs__msg__ComMsg__Sequence *
shared_msgs__msg__ComMsg__Sequence__create(size_t size);

/// Destroy array of msg/ComMsg messages.
/**
 * It calls
 * shared_msgs__msg__ComMsg__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_shared_msgs
void
shared_msgs__msg__ComMsg__Sequence__destroy(shared_msgs__msg__ComMsg__Sequence * array);

/// Check for msg/ComMsg message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_shared_msgs
bool
shared_msgs__msg__ComMsg__Sequence__are_equal(const shared_msgs__msg__ComMsg__Sequence * lhs, const shared_msgs__msg__ComMsg__Sequence * rhs);

/// Copy an array of msg/ComMsg messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_shared_msgs
bool
shared_msgs__msg__ComMsg__Sequence__copy(
  const shared_msgs__msg__ComMsg__Sequence * input,
  shared_msgs__msg__ComMsg__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // SHARED_MSGS__MSG__DETAIL__COM_MSG__FUNCTIONS_H_
