# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.266
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class FrequencyResponse(object):
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
        'execution_day': 'int',
        'frequency_type': 'str',
        'interval_month': 'int',
        'interval_week': 'int'
    }

    attribute_map = {
        'execution_day': 'executionDay',
        'frequency_type': 'frequencyType',
        'interval_month': 'intervalMonth',
        'interval_week': 'intervalWeek'
    }

    def __init__(self, execution_day=None, frequency_type=None, interval_month=None, interval_week=None, local_vars_configuration=None):  # noqa: E501
        """FrequencyResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._execution_day = None
        self._frequency_type = None
        self._interval_month = None
        self._interval_week = None
        self.discriminator = None

        if execution_day is not None:
            self.execution_day = execution_day
        if frequency_type is not None:
            self.frequency_type = frequency_type
        if interval_month is not None:
            self.interval_month = interval_month
        if interval_week is not None:
            self.interval_week = interval_week

    @property
    def execution_day(self):
        """Gets the execution_day of this FrequencyResponse.  # noqa: E501


        :return: The execution_day of this FrequencyResponse.  # noqa: E501
        :rtype: int
        """
        return self._execution_day

    @execution_day.setter
    def execution_day(self, execution_day):
        """Sets the execution_day of this FrequencyResponse.


        :param execution_day: The execution_day of this FrequencyResponse.  # noqa: E501
        :type: int
        """

        self._execution_day = execution_day

    @property
    def frequency_type(self):
        """Gets the frequency_type of this FrequencyResponse.  # noqa: E501


        :return: The frequency_type of this FrequencyResponse.  # noqa: E501
        :rtype: str
        """
        return self._frequency_type

    @frequency_type.setter
    def frequency_type(self, frequency_type):
        """Sets the frequency_type of this FrequencyResponse.


        :param frequency_type: The frequency_type of this FrequencyResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["DAILY", "EVERY_WORKING_DAY", "CALENDAR_DAY", "WEEKLY", "EVERY_TWO_WEEKS", "MONTHLY", "EVERY_TWO_MONTHS", "QUARTERLY", "SEMIANNUAL", "ANNUAL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and frequency_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `frequency_type` ({0}), must be one of {1}"  # noqa: E501
                .format(frequency_type, allowed_values)
            )

        self._frequency_type = frequency_type

    @property
    def interval_month(self):
        """Gets the interval_month of this FrequencyResponse.  # noqa: E501


        :return: The interval_month of this FrequencyResponse.  # noqa: E501
        :rtype: int
        """
        return self._interval_month

    @interval_month.setter
    def interval_month(self, interval_month):
        """Sets the interval_month of this FrequencyResponse.


        :param interval_month: The interval_month of this FrequencyResponse.  # noqa: E501
        :type: int
        """

        self._interval_month = interval_month

    @property
    def interval_week(self):
        """Gets the interval_week of this FrequencyResponse.  # noqa: E501


        :return: The interval_week of this FrequencyResponse.  # noqa: E501
        :rtype: int
        """
        return self._interval_week

    @interval_week.setter
    def interval_week(self, interval_week):
        """Sets the interval_week of this FrequencyResponse.


        :param interval_week: The interval_week of this FrequencyResponse.  # noqa: E501
        :type: int
        """

        self._interval_week = interval_week

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
        if not isinstance(other, FrequencyResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FrequencyResponse):
            return True

        return self.to_dict() != other.to_dict()
