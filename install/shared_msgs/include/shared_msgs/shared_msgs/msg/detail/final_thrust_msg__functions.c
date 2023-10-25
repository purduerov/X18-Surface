// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from shared_msgs:msg/FinalThrustMsg.idl
// generated code does not contain a copyright notice
#include "shared_msgs/msg/detail/final_thrust_msg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
shared_msgs__msg__FinalThrustMsg__init(shared_msgs__msg__FinalThrustMsg * msg)
{
  if (!msg) {
    return false;
  }
  // thrusters
  return true;
}

void
shared_msgs__msg__FinalThrustMsg__fini(shared_msgs__msg__FinalThrustMsg * msg)
{
  if (!msg) {
    return;
  }
  // thrusters
}

bool
shared_msgs__msg__FinalThrustMsg__are_equal(const shared_msgs__msg__FinalThrustMsg * lhs, const shared_msgs__msg__FinalThrustMsg * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // thrusters
  for (size_t i = 0; i < 8; ++i) {
    if (lhs->thrusters[i] != rhs->thrusters[i]) {
      return false;
    }
  }
  return true;
}

bool
shared_msgs__msg__FinalThrustMsg__copy(
  const shared_msgs__msg__FinalThrustMsg * input,
  shared_msgs__msg__FinalThrustMsg * output)
{
  if (!input || !output) {
    return false;
  }
  // thrusters
  for (size_t i = 0; i < 8; ++i) {
    output->thrusters[i] = input->thrusters[i];
  }
  return true;
}

shared_msgs__msg__FinalThrustMsg *
shared_msgs__msg__FinalThrustMsg__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  shared_msgs__msg__FinalThrustMsg * msg = (shared_msgs__msg__FinalThrustMsg *)allocator.allocate(sizeof(shared_msgs__msg__FinalThrustMsg), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(shared_msgs__msg__FinalThrustMsg));
  bool success = shared_msgs__msg__FinalThrustMsg__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
shared_msgs__msg__FinalThrustMsg__destroy(shared_msgs__msg__FinalThrustMsg * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    shared_msgs__msg__FinalThrustMsg__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
shared_msgs__msg__FinalThrustMsg__Sequence__init(shared_msgs__msg__FinalThrustMsg__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  shared_msgs__msg__FinalThrustMsg * data = NULL;

  if (size) {
    data = (shared_msgs__msg__FinalThrustMsg *)allocator.zero_allocate(size, sizeof(shared_msgs__msg__FinalThrustMsg), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = shared_msgs__msg__FinalThrustMsg__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        shared_msgs__msg__FinalThrustMsg__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
shared_msgs__msg__FinalThrustMsg__Sequence__fini(shared_msgs__msg__FinalThrustMsg__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      shared_msgs__msg__FinalThrustMsg__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

shared_msgs__msg__FinalThrustMsg__Sequence *
shared_msgs__msg__FinalThrustMsg__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  shared_msgs__msg__FinalThrustMsg__Sequence * array = (shared_msgs__msg__FinalThrustMsg__Sequence *)allocator.allocate(sizeof(shared_msgs__msg__FinalThrustMsg__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = shared_msgs__msg__FinalThrustMsg__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
shared_msgs__msg__FinalThrustMsg__Sequence__destroy(shared_msgs__msg__FinalThrustMsg__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    shared_msgs__msg__FinalThrustMsg__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
shared_msgs__msg__FinalThrustMsg__Sequence__are_equal(const shared_msgs__msg__FinalThrustMsg__Sequence * lhs, const shared_msgs__msg__FinalThrustMsg__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!shared_msgs__msg__FinalThrustMsg__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
shared_msgs__msg__FinalThrustMsg__Sequence__copy(
  const shared_msgs__msg__FinalThrustMsg__Sequence * input,
  shared_msgs__msg__FinalThrustMsg__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(shared_msgs__msg__FinalThrustMsg);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    shared_msgs__msg__FinalThrustMsg * data =
      (shared_msgs__msg__FinalThrustMsg *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!shared_msgs__msg__FinalThrustMsg__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          shared_msgs__msg__FinalThrustMsg__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!shared_msgs__msg__FinalThrustMsg__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
