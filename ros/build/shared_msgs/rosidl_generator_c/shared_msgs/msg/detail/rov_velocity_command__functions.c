// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from shared_msgs:msg/RovVelocityCommand.idl
// generated code does not contain a copyright notice
#include "shared_msgs/msg/detail/rov_velocity_command__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `twist`
#include "geometry_msgs/msg/detail/twist__functions.h"
// Member `source`
#include "rosidl_runtime_c/string_functions.h"

bool
shared_msgs__msg__RovVelocityCommand__init(shared_msgs__msg__RovVelocityCommand * msg)
{
  if (!msg) {
    return false;
  }
  // twist
  if (!geometry_msgs__msg__Twist__init(&msg->twist)) {
    shared_msgs__msg__RovVelocityCommand__fini(msg);
    return false;
  }
  // source
  if (!rosidl_runtime_c__String__init(&msg->source)) {
    shared_msgs__msg__RovVelocityCommand__fini(msg);
    return false;
  }
  // is_fine
  // multiplier
  // is_percent_power
  // is_pool_centric
  return true;
}

void
shared_msgs__msg__RovVelocityCommand__fini(shared_msgs__msg__RovVelocityCommand * msg)
{
  if (!msg) {
    return;
  }
  // twist
  geometry_msgs__msg__Twist__fini(&msg->twist);
  // source
  rosidl_runtime_c__String__fini(&msg->source);
  // is_fine
  // multiplier
  // is_percent_power
  // is_pool_centric
}

bool
shared_msgs__msg__RovVelocityCommand__are_equal(const shared_msgs__msg__RovVelocityCommand * lhs, const shared_msgs__msg__RovVelocityCommand * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // twist
  if (!geometry_msgs__msg__Twist__are_equal(
      &(lhs->twist), &(rhs->twist)))
  {
    return false;
  }
  // source
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->source), &(rhs->source)))
  {
    return false;
  }
  // is_fine
  if (lhs->is_fine != rhs->is_fine) {
    return false;
  }
  // multiplier
  if (lhs->multiplier != rhs->multiplier) {
    return false;
  }
  // is_percent_power
  if (lhs->is_percent_power != rhs->is_percent_power) {
    return false;
  }
  // is_pool_centric
  if (lhs->is_pool_centric != rhs->is_pool_centric) {
    return false;
  }
  return true;
}

bool
shared_msgs__msg__RovVelocityCommand__copy(
  const shared_msgs__msg__RovVelocityCommand * input,
  shared_msgs__msg__RovVelocityCommand * output)
{
  if (!input || !output) {
    return false;
  }
  // twist
  if (!geometry_msgs__msg__Twist__copy(
      &(input->twist), &(output->twist)))
  {
    return false;
  }
  // source
  if (!rosidl_runtime_c__String__copy(
      &(input->source), &(output->source)))
  {
    return false;
  }
  // is_fine
  output->is_fine = input->is_fine;
  // multiplier
  output->multiplier = input->multiplier;
  // is_percent_power
  output->is_percent_power = input->is_percent_power;
  // is_pool_centric
  output->is_pool_centric = input->is_pool_centric;
  return true;
}

shared_msgs__msg__RovVelocityCommand *
shared_msgs__msg__RovVelocityCommand__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  shared_msgs__msg__RovVelocityCommand * msg = (shared_msgs__msg__RovVelocityCommand *)allocator.allocate(sizeof(shared_msgs__msg__RovVelocityCommand), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(shared_msgs__msg__RovVelocityCommand));
  bool success = shared_msgs__msg__RovVelocityCommand__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
shared_msgs__msg__RovVelocityCommand__destroy(shared_msgs__msg__RovVelocityCommand * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    shared_msgs__msg__RovVelocityCommand__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
shared_msgs__msg__RovVelocityCommand__Sequence__init(shared_msgs__msg__RovVelocityCommand__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  shared_msgs__msg__RovVelocityCommand * data = NULL;

  if (size) {
    data = (shared_msgs__msg__RovVelocityCommand *)allocator.zero_allocate(size, sizeof(shared_msgs__msg__RovVelocityCommand), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = shared_msgs__msg__RovVelocityCommand__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        shared_msgs__msg__RovVelocityCommand__fini(&data[i - 1]);
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
shared_msgs__msg__RovVelocityCommand__Sequence__fini(shared_msgs__msg__RovVelocityCommand__Sequence * array)
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
      shared_msgs__msg__RovVelocityCommand__fini(&array->data[i]);
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

shared_msgs__msg__RovVelocityCommand__Sequence *
shared_msgs__msg__RovVelocityCommand__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  shared_msgs__msg__RovVelocityCommand__Sequence * array = (shared_msgs__msg__RovVelocityCommand__Sequence *)allocator.allocate(sizeof(shared_msgs__msg__RovVelocityCommand__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = shared_msgs__msg__RovVelocityCommand__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
shared_msgs__msg__RovVelocityCommand__Sequence__destroy(shared_msgs__msg__RovVelocityCommand__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    shared_msgs__msg__RovVelocityCommand__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
shared_msgs__msg__RovVelocityCommand__Sequence__are_equal(const shared_msgs__msg__RovVelocityCommand__Sequence * lhs, const shared_msgs__msg__RovVelocityCommand__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!shared_msgs__msg__RovVelocityCommand__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
shared_msgs__msg__RovVelocityCommand__Sequence__copy(
  const shared_msgs__msg__RovVelocityCommand__Sequence * input,
  shared_msgs__msg__RovVelocityCommand__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(shared_msgs__msg__RovVelocityCommand);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    shared_msgs__msg__RovVelocityCommand * data =
      (shared_msgs__msg__RovVelocityCommand *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!shared_msgs__msg__RovVelocityCommand__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          shared_msgs__msg__RovVelocityCommand__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!shared_msgs__msg__RovVelocityCommand__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
