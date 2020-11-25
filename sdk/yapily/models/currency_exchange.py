# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.280
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class CurrencyExchange(object):
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
        'source_currency': 'str',
        'target_currency': 'str',
        'unit_currency': 'str',
        'exchange_rate': 'float'
    }

    attribute_map = {
        'source_currency': 'sourceCurrency',
        'target_currency': 'targetCurrency',
        'unit_currency': 'unitCurrency',
        'exchange_rate': 'exchangeRate'
    }

    def __init__(self, source_currency=None, target_currency=None, unit_currency=None, exchange_rate=None, local_vars_configuration=None):  # noqa: E501
        """CurrencyExchange - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source_currency = None
        self._target_currency = None
        self._unit_currency = None
        self._exchange_rate = None
        self.discriminator = None

        if source_currency is not None:
            self.source_currency = source_currency
        if target_currency is not None:
            self.target_currency = target_currency
        if unit_currency is not None:
            self.unit_currency = unit_currency
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate

    @property
    def source_currency(self):
        """Gets the source_currency of this CurrencyExchange.  # noqa: E501

        ISO 4217 currency code denoting the currency of the creditor  # noqa: E501

        :return: The source_currency of this CurrencyExchange.  # noqa: E501
        :rtype: str
        """
        return self._source_currency

    @source_currency.setter
    def source_currency(self, source_currency):
        """Sets the source_currency of this CurrencyExchange.

        ISO 4217 currency code denoting the currency of the creditor  # noqa: E501

        :param source_currency: The source_currency of this CurrencyExchange.  # noqa: E501
        :type: str
        """

        self._source_currency = source_currency

    @property
    def target_currency(self):
        """Gets the target_currency of this CurrencyExchange.  # noqa: E501

        ISO 4217 currency code denoting the currency of the debtor  # noqa: E501

        :return: The target_currency of this CurrencyExchange.  # noqa: E501
        :rtype: str
        """
        return self._target_currency

    @target_currency.setter
    def target_currency(self, target_currency):
        """Sets the target_currency of this CurrencyExchange.

        ISO 4217 currency code denoting the currency of the debtor  # noqa: E501

        :param target_currency: The target_currency of this CurrencyExchange.  # noqa: E501
        :type: str
        """

        self._target_currency = target_currency

    @property
    def unit_currency(self):
        """Gets the unit_currency of this CurrencyExchange.  # noqa: E501

        ISO 4217 currency code denoting the currency used to set the exchange rate (GBP is the unit currency in the conversion of 1 GBP = x CUR)  # noqa: E501

        :return: The unit_currency of this CurrencyExchange.  # noqa: E501
        :rtype: str
        """
        return self._unit_currency

    @unit_currency.setter
    def unit_currency(self, unit_currency):
        """Sets the unit_currency of this CurrencyExchange.

        ISO 4217 currency code denoting the currency used to set the exchange rate (GBP is the unit currency in the conversion of 1 GBP = x CUR)  # noqa: E501

        :param unit_currency: The unit_currency of this CurrencyExchange.  # noqa: E501
        :type: str
        """

        self._unit_currency = unit_currency

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this CurrencyExchange.  # noqa: E501

        Currency exchange rate  # noqa: E501

        :return: The exchange_rate of this CurrencyExchange.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this CurrencyExchange.

        Currency exchange rate  # noqa: E501

        :param exchange_rate: The exchange_rate of this CurrencyExchange.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

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
        if not isinstance(other, CurrencyExchange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurrencyExchange):
            return True

        return self.to_dict() != other.to_dict()
