# generated from rosidl_generator_py/resource/_idl.py.em
# with input from shared_msgs:msg/RovVelocityCommand.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RovVelocityCommand(type):
    """Metaclass of message 'RovVelocityCommand'."""

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
                'shared_msgs.msg.RovVelocityCommand')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__rov_velocity_command
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__rov_velocity_command
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__rov_velocity_command
            cls._TYPE_SUPPORT = module.type_support_msg__msg__rov_velocity_command
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__rov_velocity_command

            from geometry_msgs.msg import Twist
            if Twist.__class__._TYPE_SUPPORT is None:
                Twist.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RovVelocityCommand(metaclass=Metaclass_RovVelocityCommand):
    """Message class 'RovVelocityCommand'."""

    __slots__ = [
        '_twist',
        '_source',
        '_is_fine',
        '_multiplier',
        '_is_percent_power',
        '_is_pool_centric',
    ]

    _fields_and_field_types = {
        'twist': 'geometry_msgs/Twist',
        'source': 'string',
        'is_fine': 'boolean',
        'multiplier': 'float',
        'is_percent_power': 'boolean',
        'is_pool_centric': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Twist'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from geometry_msgs.msg import Twist
        self.twist = kwargs.get('twist', Twist())
        self.source = kwargs.get('source', str())
        self.is_fine = kwargs.get('is_fine', bool())
        self.multiplier = kwargs.get('multiplier', float())
        self.is_percent_power = kwargs.get('is_percent_power', bool())
        self.is_pool_centric = kwargs.get('is_pool_centric', bool())

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
        if self.twist != other.twist:
            return False
        if self.source != other.source:
            return False
        if self.is_fine != other.is_fine:
            return False
        if self.multiplier != other.multiplier:
            return False
        if self.is_percent_power != other.is_percent_power:
            return False
        if self.is_pool_centric != other.is_pool_centric:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def twist(self):
        """Message field 'twist'."""
        return self._twist

    @twist.setter
    def twist(self, value):
        if __debug__:
            from geometry_msgs.msg import Twist
            assert \
                isinstance(value, Twist), \
                "The 'twist' field must be a sub message of type 'Twist'"
        self._twist = value

    @builtins.property
    def source(self):
        """Message field 'source'."""
        return self._source

    @source.setter
    def source(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'source' field must be of type 'str'"
        self._source = value

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

    @builtins.property
    def is_percent_power(self):
        """Message field 'is_percent_power'."""
        return self._is_percent_power

    @is_percent_power.setter
    def is_percent_power(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'is_percent_power' field must be of type 'bool'"
        self._is_percent_power = value

    @builtins.property
    def is_pool_centric(self):
        """Message field 'is_pool_centric'."""
        return self._is_pool_centric

    @is_pool_centric.setter
    def is_pool_centric(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'is_pool_centric' field must be of type 'bool'"
        self._is_pool_centric = value
