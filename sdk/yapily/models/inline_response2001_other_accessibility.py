# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.318
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class InlineResponse2001OtherAccessibility(object):
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
        'code': 'str',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'code': 'Code',
        'description': 'Description',
        'name': 'Name'
    }

    def __init__(self, code=None, description=None, name=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2001OtherAccessibility - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._description = None
        self._name = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name

    @property
    def code(self):
        """Gets the code of this InlineResponse2001OtherAccessibility.  # noqa: E501


        :return: The code of this InlineResponse2001OtherAccessibility.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InlineResponse2001OtherAccessibility.


        :param code: The code of this InlineResponse2001OtherAccessibility.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def description(self):
        """Gets the description of this InlineResponse2001OtherAccessibility.  # noqa: E501


        :return: The description of this InlineResponse2001OtherAccessibility.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse2001OtherAccessibility.


        :param description: The description of this InlineResponse2001OtherAccessibility.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this InlineResponse2001OtherAccessibility.  # noqa: E501


        :return: The name of this InlineResponse2001OtherAccessibility.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2001OtherAccessibility.


        :param name: The name of this InlineResponse2001OtherAccessibility.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, InlineResponse2001OtherAccessibility):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2001OtherAccessibility):
            return True

        return self.to_dict() != other.to_dict()
