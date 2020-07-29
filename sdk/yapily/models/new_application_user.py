# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.216
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class NewApplicationUser(object):
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
        'application_user_id': 'str',
        'reference_id': 'str'
    }

    attribute_map = {
        'application_user_id': 'applicationUserId',
        'reference_id': 'referenceId'
    }

    def __init__(self, application_user_id=None, reference_id=None, local_vars_configuration=None):  # noqa: E501
        """NewApplicationUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application_user_id = None
        self._reference_id = None
        self.discriminator = None

        if application_user_id is not None:
            self.application_user_id = application_user_id
        if reference_id is not None:
            self.reference_id = reference_id

    @property
    def application_user_id(self):
        """Gets the application_user_id of this NewApplicationUser.  # noqa: E501


        :return: The application_user_id of this NewApplicationUser.  # noqa: E501
        :rtype: str
        """
        return self._application_user_id

    @application_user_id.setter
    def application_user_id(self, application_user_id):
        """Sets the application_user_id of this NewApplicationUser.


        :param application_user_id: The application_user_id of this NewApplicationUser.  # noqa: E501
        :type: str
        """

        self._application_user_id = application_user_id

    @property
    def reference_id(self):
        """Gets the reference_id of this NewApplicationUser.  # noqa: E501


        :return: The reference_id of this NewApplicationUser.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this NewApplicationUser.


        :param reference_id: The reference_id of this NewApplicationUser.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

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
        if not isinstance(other, NewApplicationUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewApplicationUser):
            return True

        return self.to_dict() != other.to_dict()
