// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from shared_msgs:msg/RovVelocityCommand.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "shared_msgs/msg/detail/rov_velocity_command__struct.h"
#include "shared_msgs/msg/detail/rov_velocity_command__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool geometry_msgs__msg__twist__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * geometry_msgs__msg__twist__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool shared_msgs__msg__rov_velocity_command__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[57];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("shared_msgs.msg._rov_velocity_command.RovVelocityCommand", full_classname_dest, 56) == 0);
  }
  shared_msgs__msg__RovVelocityCommand * ros_message = _ros_message;
  {  // twist
    PyObject * field = PyObject_GetAttrString(_pymsg, "twist");
    if (!field) {
      return false;
    }
    if (!geometry_msgs__msg__twist__convert_from_py(field, &ros_message->twist)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // source
    PyObject * field = PyObject_GetAttrString(_pymsg, "source");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->source, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // is_fine
    PyObject * field = PyObject_GetAttrString(_pymsg, "is_fine");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->is_fine = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // multiplier
    PyObject * field = PyObject_GetAttrString(_pymsg, "multiplier");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->multiplier = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // is_percent_power
    PyObject * field = PyObject_GetAttrString(_pymsg, "is_percent_power");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->is_percent_power = (Py_True == field);
    Py_DECREF(field);
  }
  {  // is_pool_centric
    PyObject * field = PyObject_GetAttrString(_pymsg, "is_pool_centric");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->is_pool_centric = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * shared_msgs__msg__rov_velocity_command__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of RovVelocityCommand */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("shared_msgs.msg._rov_velocity_command");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "RovVelocityCommand");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  shared_msgs__msg__RovVelocityCommand * ros_message = (shared_msgs__msg__RovVelocityCommand *)raw_ros_message;
  {  // twist
    PyObject * field = NULL;
    field = geometry_msgs__msg__twist__convert_to_py(&ros_message->twist);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "twist", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // source
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->source.data,
      strlen(ros_message->source.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "source", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // is_fine
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->is_fine);
    {
      int rc = PyObject_SetAttrString(_pymessage, "is_fine", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // multiplier
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->multiplier);
    {
      int rc = PyObject_SetAttrString(_pymessage, "multiplier", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // is_percent_power
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->is_percent_power ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "is_percent_power", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // is_pool_centric
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->is_pool_centric ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "is_pool_centric", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
