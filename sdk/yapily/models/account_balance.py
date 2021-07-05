# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.361
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class AccountBalance(object):
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
        'type': 'str',
        'date_time': 'datetime',
        'balance_amount': 'Amount',
        'credit_line_included': 'bool',
        'credit_lines': 'list[CreditLine]'
    }

    attribute_map = {
        'type': 'type',
        'date_time': 'dateTime',
        'balance_amount': 'balanceAmount',
        'credit_line_included': 'creditLineIncluded',
        'credit_lines': 'creditLines'
    }

    def __init__(self, type=None, date_time=None, balance_amount=None, credit_line_included=None, credit_lines=None, local_vars_configuration=None):  # noqa: E501
        """AccountBalance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._date_time = None
        self._balance_amount = None
        self._credit_line_included = None
        self._credit_lines = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if date_time is not None:
            self.date_time = date_time
        if balance_amount is not None:
            self.balance_amount = balance_amount
        if credit_line_included is not None:
            self.credit_line_included = credit_line_included
        if credit_lines is not None:
            self.credit_lines = credit_lines

    @property
    def type(self):
        """Gets the type of this AccountBalance.  # noqa: E501


        :return: The type of this AccountBalance.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountBalance.


        :param type: The type of this AccountBalance.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLOSING_AVAILABLE", "CLOSING_BOOKED", "CLOSING_CLEARED", "EXPECTED", "FORWARD_AVAILABLE", "INFORMATION", "INTERIM_AVAILABLE", "INTERIM_BOOKED", "INTERIM_CLEARED", "OPENING_AVAILABLE", "OPENING_BOOKED", "OPENING_CLEARED", "PREVIOUSLY_CLOSED_BOOKED", "AUTHORISED", "OTHER", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def date_time(self):
        """Gets the date_time of this AccountBalance.  # noqa: E501

        Timestamp of the last change of the balance amount  # noqa: E501

        :return: The date_time of this AccountBalance.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this AccountBalance.

        Timestamp of the last change of the balance amount  # noqa: E501

        :param date_time: The date_time of this AccountBalance.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def balance_amount(self):
        """Gets the balance_amount of this AccountBalance.  # noqa: E501


        :return: The balance_amount of this AccountBalance.  # noqa: E501
        :rtype: Amount
        """
        return self._balance_amount

    @balance_amount.setter
    def balance_amount(self, balance_amount):
        """Sets the balance_amount of this AccountBalance.


        :param balance_amount: The balance_amount of this AccountBalance.  # noqa: E501
        :type: Amount
        """

        self._balance_amount = balance_amount

    @property
    def credit_line_included(self):
        """Gets the credit_line_included of this AccountBalance.  # noqa: E501

        Indicates whether or not the credit line is included in the balance  # noqa: E501

        :return: The credit_line_included of this AccountBalance.  # noqa: E501
        :rtype: bool
        """
        return self._credit_line_included

    @credit_line_included.setter
    def credit_line_included(self, credit_line_included):
        """Sets the credit_line_included of this AccountBalance.

        Indicates whether or not the credit line is included in the balance  # noqa: E501

        :param credit_line_included: The credit_line_included of this AccountBalance.  # noqa: E501
        :type: bool
        """

        self._credit_line_included = credit_line_included

    @property
    def credit_lines(self):
        """Gets the credit_lines of this AccountBalance.  # noqa: E501


        :return: The credit_lines of this AccountBalance.  # noqa: E501
        :rtype: list[CreditLine]
        """
        return self._credit_lines

    @credit_lines.setter
    def credit_lines(self, credit_lines):
        """Sets the credit_lines of this AccountBalance.


        :param credit_lines: The credit_lines of this AccountBalance.  # noqa: E501
        :type: list[CreditLine]
        """

        self._credit_lines = credit_lines

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
        if not isinstance(other, AccountBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountBalance):
            return True

        return self.to_dict() != other.to_dict()
