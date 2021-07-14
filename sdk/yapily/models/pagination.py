# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.365
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class Pagination(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'next': 'Next',
        '_self': 'FilterAndSort',
        'total_count': 'int'
    }

    attribute_map = {
        'next': 'next',
        '_self': 'self',
        'total_count': 'totalCount'
    }

    def __init__(self, next=None, _self=None, total_count=None, local_vars_configuration=None):  # noqa: E501
        """Pagination - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._next = None
        self.__self = None
        self._total_count = None
        self.discriminator = None

        if next is not None:
            self.next = next
        if _self is not None:
            self._self = _self
        if total_count is not None:
            self.total_count = total_count

    @property
    def next(self):
        """Gets the next of this Pagination.  # noqa: E501


        :return: The next of this Pagination.  # noqa: E501
        :rtype: Next
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Pagination.


        :param next: The next of this Pagination.  # noqa: E501
        :type: Next
        """

        self._next = next

    @property
    def _self(self):
        """Gets the _self of this Pagination.  # noqa: E501


        :return: The _self of this Pagination.  # noqa: E501
        :rtype: FilterAndSort
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this Pagination.


        :param _self: The _self of this Pagination.  # noqa: E501
        :type: FilterAndSort
        """

        self.__self = _self

    @property
    def total_count(self):
        """Gets the total_count of this Pagination.  # noqa: E501


        :return: The total_count of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this Pagination.


        :param total_count: The total_count of this Pagination.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Pagination):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Pagination):
            return True

        return self.to_dict() != other.to_dict()
