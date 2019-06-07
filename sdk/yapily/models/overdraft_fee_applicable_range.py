# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.111
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OverdraftFeeApplicableRange(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'maximum_amount': 'str',
        'maximum_rate': 'str',
        'minimum_amount': 'str',
        'minimum_rate': 'str'
    }

    attribute_map = {
        'maximum_amount': 'MaximumAmount',
        'maximum_rate': 'MaximumRate',
        'minimum_amount': 'MinimumAmount',
        'minimum_rate': 'MinimumRate'
    }

    def __init__(self, maximum_amount=None, maximum_rate=None, minimum_amount=None, minimum_rate=None):  # noqa: E501
        """OverdraftFeeApplicableRange - a model defined in Swagger"""  # noqa: E501

        self._maximum_amount = None
        self._maximum_rate = None
        self._minimum_amount = None
        self._minimum_rate = None
        self.discriminator = None

        if maximum_amount is not None:
            self.maximum_amount = maximum_amount
        if maximum_rate is not None:
            self.maximum_rate = maximum_rate
        if minimum_amount is not None:
            self.minimum_amount = minimum_amount
        if minimum_rate is not None:
            self.minimum_rate = minimum_rate

    @property
    def maximum_amount(self):
        """Gets the maximum_amount of this OverdraftFeeApplicableRange.  # noqa: E501


        :return: The maximum_amount of this OverdraftFeeApplicableRange.  # noqa: E501
        :rtype: str
        """
        return self._maximum_amount

    @maximum_amount.setter
    def maximum_amount(self, maximum_amount):
        """Sets the maximum_amount of this OverdraftFeeApplicableRange.


        :param maximum_amount: The maximum_amount of this OverdraftFeeApplicableRange.  # noqa: E501
        :type: str
        """

        self._maximum_amount = maximum_amount

    @property
    def maximum_rate(self):
        """Gets the maximum_rate of this OverdraftFeeApplicableRange.  # noqa: E501


        :return: The maximum_rate of this OverdraftFeeApplicableRange.  # noqa: E501
        :rtype: str
        """
        return self._maximum_rate

    @maximum_rate.setter
    def maximum_rate(self, maximum_rate):
        """Sets the maximum_rate of this OverdraftFeeApplicableRange.


        :param maximum_rate: The maximum_rate of this OverdraftFeeApplicableRange.  # noqa: E501
        :type: str
        """

        self._maximum_rate = maximum_rate

    @property
    def minimum_amount(self):
        """Gets the minimum_amount of this OverdraftFeeApplicableRange.  # noqa: E501


        :return: The minimum_amount of this OverdraftFeeApplicableRange.  # noqa: E501
        :rtype: str
        """
        return self._minimum_amount

    @minimum_amount.setter
    def minimum_amount(self, minimum_amount):
        """Sets the minimum_amount of this OverdraftFeeApplicableRange.


        :param minimum_amount: The minimum_amount of this OverdraftFeeApplicableRange.  # noqa: E501
        :type: str
        """

        self._minimum_amount = minimum_amount

    @property
    def minimum_rate(self):
        """Gets the minimum_rate of this OverdraftFeeApplicableRange.  # noqa: E501


        :return: The minimum_rate of this OverdraftFeeApplicableRange.  # noqa: E501
        :rtype: str
        """
        return self._minimum_rate

    @minimum_rate.setter
    def minimum_rate(self, minimum_rate):
        """Sets the minimum_rate of this OverdraftFeeApplicableRange.


        :param minimum_rate: The minimum_rate of this OverdraftFeeApplicableRange.  # noqa: E501
        :type: str
        """

        self._minimum_rate = minimum_rate

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, OverdraftFeeApplicableRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
