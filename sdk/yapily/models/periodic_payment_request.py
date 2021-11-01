# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.159.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class PeriodicPaymentRequest(object):
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
        'frequency': 'FrequencyRequest',
        'number_of_payments': 'int',
        'next_payment_date_time': 'datetime',
        'next_payment_amount': 'Amount',
        'final_payment_date_time': 'datetime',
        'final_payment_amount': 'Amount'
    }

    attribute_map = {
        'frequency': 'frequency',
        'number_of_payments': 'numberOfPayments',
        'next_payment_date_time': 'nextPaymentDateTime',
        'next_payment_amount': 'nextPaymentAmount',
        'final_payment_date_time': 'finalPaymentDateTime',
        'final_payment_amount': 'finalPaymentAmount'
    }

    def __init__(self, frequency=None, number_of_payments=None, next_payment_date_time=None, next_payment_amount=None, final_payment_date_time=None, final_payment_amount=None, local_vars_configuration=None):  # noqa: E501
        """PeriodicPaymentRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._frequency = None
        self._number_of_payments = None
        self._next_payment_date_time = None
        self._next_payment_amount = None
        self._final_payment_date_time = None
        self._final_payment_amount = None
        self.discriminator = None

        self.frequency = frequency
        if number_of_payments is not None:
            self.number_of_payments = number_of_payments
        if next_payment_date_time is not None:
            self.next_payment_date_time = next_payment_date_time
        if next_payment_amount is not None:
            self.next_payment_amount = next_payment_amount
        if final_payment_date_time is not None:
            self.final_payment_date_time = final_payment_date_time
        if final_payment_amount is not None:
            self.final_payment_amount = final_payment_amount

    @property
    def frequency(self):
        """Gets the frequency of this PeriodicPaymentRequest.  # noqa: E501


        :return: The frequency of this PeriodicPaymentRequest.  # noqa: E501
        :rtype: FrequencyRequest
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this PeriodicPaymentRequest.


        :param frequency: The frequency of this PeriodicPaymentRequest.  # noqa: E501
        :type: FrequencyRequest
        """
        if self.local_vars_configuration.client_side_validation and frequency is None:  # noqa: E501
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501

        self._frequency = frequency

    @property
    def number_of_payments(self):
        """Gets the number_of_payments of this PeriodicPaymentRequest.  # noqa: E501


        :return: The number_of_payments of this PeriodicPaymentRequest.  # noqa: E501
        :rtype: int
        """
        return self._number_of_payments

    @number_of_payments.setter
    def number_of_payments(self, number_of_payments):
        """Sets the number_of_payments of this PeriodicPaymentRequest.


        :param number_of_payments: The number_of_payments of this PeriodicPaymentRequest.  # noqa: E501
        :type: int
        """

        self._number_of_payments = number_of_payments

    @property
    def next_payment_date_time(self):
        """Gets the next_payment_date_time of this PeriodicPaymentRequest.  # noqa: E501


        :return: The next_payment_date_time of this PeriodicPaymentRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._next_payment_date_time

    @next_payment_date_time.setter
    def next_payment_date_time(self, next_payment_date_time):
        """Sets the next_payment_date_time of this PeriodicPaymentRequest.


        :param next_payment_date_time: The next_payment_date_time of this PeriodicPaymentRequest.  # noqa: E501
        :type: datetime
        """

        self._next_payment_date_time = next_payment_date_time

    @property
    def next_payment_amount(self):
        """Gets the next_payment_amount of this PeriodicPaymentRequest.  # noqa: E501


        :return: The next_payment_amount of this PeriodicPaymentRequest.  # noqa: E501
        :rtype: Amount
        """
        return self._next_payment_amount

    @next_payment_amount.setter
    def next_payment_amount(self, next_payment_amount):
        """Sets the next_payment_amount of this PeriodicPaymentRequest.


        :param next_payment_amount: The next_payment_amount of this PeriodicPaymentRequest.  # noqa: E501
        :type: Amount
        """

        self._next_payment_amount = next_payment_amount

    @property
    def final_payment_date_time(self):
        """Gets the final_payment_date_time of this PeriodicPaymentRequest.  # noqa: E501


        :return: The final_payment_date_time of this PeriodicPaymentRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._final_payment_date_time

    @final_payment_date_time.setter
    def final_payment_date_time(self, final_payment_date_time):
        """Sets the final_payment_date_time of this PeriodicPaymentRequest.


        :param final_payment_date_time: The final_payment_date_time of this PeriodicPaymentRequest.  # noqa: E501
        :type: datetime
        """

        self._final_payment_date_time = final_payment_date_time

    @property
    def final_payment_amount(self):
        """Gets the final_payment_amount of this PeriodicPaymentRequest.  # noqa: E501


        :return: The final_payment_amount of this PeriodicPaymentRequest.  # noqa: E501
        :rtype: Amount
        """
        return self._final_payment_amount

    @final_payment_amount.setter
    def final_payment_amount(self, final_payment_amount):
        """Sets the final_payment_amount of this PeriodicPaymentRequest.


        :param final_payment_amount: The final_payment_amount of this PeriodicPaymentRequest.  # noqa: E501
        :type: Amount
        """

        self._final_payment_amount = final_payment_amount

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
        if not isinstance(other, PeriodicPaymentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PeriodicPaymentRequest):
            return True

        return self.to_dict() != other.to_dict()
