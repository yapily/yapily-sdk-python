# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.209
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class ExchangeRateInformation(object):
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
        'foreign_exchange_contract_reference': 'str',
        'rate': 'float',
        'rate_type': 'str',
        'unit_currency': 'str'
    }

    attribute_map = {
        'foreign_exchange_contract_reference': 'foreignExchangeContractReference',
        'rate': 'rate',
        'rate_type': 'rateType',
        'unit_currency': 'unitCurrency'
    }

    def __init__(self, foreign_exchange_contract_reference=None, rate=None, rate_type=None, unit_currency=None, local_vars_configuration=None):  # noqa: E501
        """ExchangeRateInformation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._foreign_exchange_contract_reference = None
        self._rate = None
        self._rate_type = None
        self._unit_currency = None
        self.discriminator = None

        if foreign_exchange_contract_reference is not None:
            self.foreign_exchange_contract_reference = foreign_exchange_contract_reference
        if rate is not None:
            self.rate = rate
        if rate_type is not None:
            self.rate_type = rate_type
        if unit_currency is not None:
            self.unit_currency = unit_currency

    @property
    def foreign_exchange_contract_reference(self):
        """Gets the foreign_exchange_contract_reference of this ExchangeRateInformation.  # noqa: E501


        :return: The foreign_exchange_contract_reference of this ExchangeRateInformation.  # noqa: E501
        :rtype: str
        """
        return self._foreign_exchange_contract_reference

    @foreign_exchange_contract_reference.setter
    def foreign_exchange_contract_reference(self, foreign_exchange_contract_reference):
        """Sets the foreign_exchange_contract_reference of this ExchangeRateInformation.


        :param foreign_exchange_contract_reference: The foreign_exchange_contract_reference of this ExchangeRateInformation.  # noqa: E501
        :type: str
        """

        self._foreign_exchange_contract_reference = foreign_exchange_contract_reference

    @property
    def rate(self):
        """Gets the rate of this ExchangeRateInformation.  # noqa: E501


        :return: The rate of this ExchangeRateInformation.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this ExchangeRateInformation.


        :param rate: The rate of this ExchangeRateInformation.  # noqa: E501
        :type: float
        """

        self._rate = rate

    @property
    def rate_type(self):
        """Gets the rate_type of this ExchangeRateInformation.  # noqa: E501


        :return: The rate_type of this ExchangeRateInformation.  # noqa: E501
        :rtype: str
        """
        return self._rate_type

    @rate_type.setter
    def rate_type(self, rate_type):
        """Sets the rate_type of this ExchangeRateInformation.


        :param rate_type: The rate_type of this ExchangeRateInformation.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTUAL", "AGREED", "INDICATIVE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and rate_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `rate_type` ({0}), must be one of {1}"  # noqa: E501
                .format(rate_type, allowed_values)
            )

        self._rate_type = rate_type

    @property
    def unit_currency(self):
        """Gets the unit_currency of this ExchangeRateInformation.  # noqa: E501


        :return: The unit_currency of this ExchangeRateInformation.  # noqa: E501
        :rtype: str
        """
        return self._unit_currency

    @unit_currency.setter
    def unit_currency(self, unit_currency):
        """Sets the unit_currency of this ExchangeRateInformation.


        :param unit_currency: The unit_currency of this ExchangeRateInformation.  # noqa: E501
        :type: str
        """

        self._unit_currency = unit_currency

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
        if not isinstance(other, ExchangeRateInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExchangeRateInformation):
            return True

        return self.to_dict() != other.to_dict()
