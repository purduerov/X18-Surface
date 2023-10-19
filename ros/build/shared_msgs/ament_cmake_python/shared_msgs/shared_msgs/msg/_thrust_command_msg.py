# generated from rosidl_generator_py/resource/_idl.py.em
# with input from shared_msgs:msg/ThrustCommandMsg.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

# Member 'desired_thrust'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ThrustCommandMsg(type):
    """Metaclass of message 'ThrustCommandMsg'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('shared_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'shared_msgs.msg.ThrustCommandMsg')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__thrust_command_msg
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__thrust_command_msg
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__thrust_command_msg
            cls._TYPE_SUPPORT = module.type_support_msg__msg__thrust_command_msg
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__thrust_command_msg

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ThrustCommandMsg(metaclass=Metaclass_ThrustCommandMsg):
    """Message class 'ThrustCommandMsg'."""

    __slots__ = [
        '_desired_thrust',
        '_is_fine',
        '_multiplier',
    ]

    _fields_and_field_types = {
        'desired_thrust': 'float[6]',
        'is_fine': 'boolean',
        'multiplier': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 6),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        if 'desired_thrust' not in kwargs:
            self.desired_thrust = numpy.zeros(6, dtype=numpy.float32)
        else:
            self.desired_thrust = numpy.array(kwargs.get('desired_thrust'), dtype=numpy.float32)
            assert self.desired_thrust.shape == (6, )
        self.is_fine = kwargs.get('is_fine', bool())
        self.multiplier = kwargs.get('multiplier', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if all(self.desired_thrust != other.desired_thrust):
            return False
        if self.is_fine != other.is_fine:
            return False
        if self.multiplier != other.multiplier:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def desired_thrust(self):
        """Message field 'desired_thrust'."""
        return self._desired_thrust

    @desired_thrust.setter
    def desired_thrust(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'desired_thrust' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 6, \
                "The 'desired_thrust' numpy.ndarray() must have a size of 6"
            self._desired_thrust = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 6 and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'desired_thrust' field must be a set or sequence with length 6 and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._desired_thrust = numpy.array(value, dtype=numpy.float32)

    @builtins.property
    def is_fine(self):
        """Message field 'is_fine'."""
        return self._is_fine

    @is_fine.setter
    def is_fine(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'is_fine' field must be of type 'bool'"
        self._is_fine = value

    @builtins.property
    def multiplier(self):
        """Message field 'multiplier'."""
        return self._multiplier

    @multiplier.setter
    def multiplier(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'multiplier' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'multiplier' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._multiplier = value
