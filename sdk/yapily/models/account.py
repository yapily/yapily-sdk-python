# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.297
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class Account(object):
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
        'id': 'str',
        'type': 'str',
        'description': 'str',
        'balance': 'float',
        'currency': 'str',
        'usage_type': 'str',
        'account_type': 'str',
        'nickname': 'str',
        'details': 'str',
        'account_names': 'list[AccountName]',
        'account_identifications': 'list[AccountIdentification]',
        'account_balances': 'list[AccountBalance]'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'description': 'description',
        'balance': 'balance',
        'currency': 'currency',
        'usage_type': 'usageType',
        'account_type': 'accountType',
        'nickname': 'nickname',
        'details': 'details',
        'account_names': 'accountNames',
        'account_identifications': 'accountIdentifications',
        'account_balances': 'accountBalances'
    }

    def __init__(self, id=None, type=None, description=None, balance=None, currency=None, usage_type=None, account_type=None, nickname=None, details=None, account_names=None, account_identifications=None, account_balances=None, local_vars_configuration=None):  # noqa: E501
        """Account - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._description = None
        self._balance = None
        self._currency = None
        self._usage_type = None
        self._account_type = None
        self._nickname = None
        self._details = None
        self._account_names = None
        self._account_identifications = None
        self._account_balances = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if balance is not None:
            self.balance = balance
        if currency is not None:
            self.currency = currency
        if usage_type is not None:
            self.usage_type = usage_type
        if account_type is not None:
            self.account_type = account_type
        if nickname is not None:
            self.nickname = nickname
        if details is not None:
            self.details = details
        if account_names is not None:
            self.account_names = account_names
        if account_identifications is not None:
            self.account_identifications = account_identifications
        if account_balances is not None:
            self.account_balances = account_balances

    @property
    def id(self):
        """Gets the id of this Account.  # noqa: E501

        Account Id returned by the institution if present  # noqa: E501

        :return: The id of this Account.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Account.

        Account Id returned by the institution if present  # noqa: E501

        :param id: The id of this Account.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Account.  # noqa: E501


        :return: The type of this Account.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Account.


        :param type: The type of this Account.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this Account.  # noqa: E501

        Product name as defined by the financial institution for this account  # noqa: E501

        :return: The description of this Account.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Account.

        Product name as defined by the financial institution for this account  # noqa: E501

        :param description: The description of this Account.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def balance(self):
        """Gets the balance of this Account.  # noqa: E501


        :return: The balance of this Account.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Account.


        :param balance: The balance of this Account.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def currency(self):
        """Gets the currency of this Account.  # noqa: E501

        ISO 4217 currency code  # noqa: E501

        :return: The currency of this Account.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Account.

        ISO 4217 currency code  # noqa: E501

        :param currency: The currency of this Account.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def usage_type(self):
        """Gets the usage_type of this Account.  # noqa: E501


        :return: The usage_type of this Account.  # noqa: E501
        :rtype: str
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        """Sets the usage_type of this Account.


        :param usage_type: The usage_type of this Account.  # noqa: E501
        :type: str
        """
        allowed_values = ["PERSONAL", "BUSINESS", "OTHER", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and usage_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `usage_type` ({0}), must be one of {1}"  # noqa: E501
                .format(usage_type, allowed_values)
            )

        self._usage_type = usage_type

    @property
    def account_type(self):
        """Gets the account_type of this Account.  # noqa: E501


        :return: The account_type of this Account.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this Account.


        :param account_type: The account_type of this Account.  # noqa: E501
        :type: str
        """
        allowed_values = ["CASH_TRADING", "CASH_INCOME", "CASH_PAYMENT", "CHARGE_CARD", "CHARGES", "COMMISSION", "CREDIT_CARD", "CURRENT", "E_MONEY", "LIMITED_LIQUIDITY_SAVINGS_ACCOUNT", "LOAN", "MARGINAL_LENDING", "MONEY_MARKET", "MORTGAGE", "NON_RESIDENT_EXTERNAL", "OTHER", "OVERDRAFT", "OVERNIGHT_DEPOSIT", "PREPAID_CARD", "SALARY", "SAVINGS", "SETTLEMENT", "TAX", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and account_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def nickname(self):
        """Gets the nickname of this Account.  # noqa: E501

        Name of the account as defined by the financial institution or the end user  # noqa: E501

        :return: The nickname of this Account.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this Account.

        Name of the account as defined by the financial institution or the end user  # noqa: E501

        :param nickname: The nickname of this Account.  # noqa: E501
        :type: str
        """

        self._nickname = nickname

    @property
    def details(self):
        """Gets the details of this Account.  # noqa: E501

        Specifications that might be provided by the institution - characteristics of the account - characteristics of the relevant card  # noqa: E501

        :return: The details of this Account.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Account.

        Specifications that might be provided by the institution - characteristics of the account - characteristics of the relevant card  # noqa: E501

        :param details: The details of this Account.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def account_names(self):
        """Gets the account_names of this Account.  # noqa: E501


        :return: The account_names of this Account.  # noqa: E501
        :rtype: list[AccountName]
        """
        return self._account_names

    @account_names.setter
    def account_names(self, account_names):
        """Sets the account_names of this Account.


        :param account_names: The account_names of this Account.  # noqa: E501
        :type: list[AccountName]
        """

        self._account_names = account_names

    @property
    def account_identifications(self):
        """Gets the account_identifications of this Account.  # noqa: E501


        :return: The account_identifications of this Account.  # noqa: E501
        :rtype: list[AccountIdentification]
        """
        return self._account_identifications

    @account_identifications.setter
    def account_identifications(self, account_identifications):
        """Sets the account_identifications of this Account.


        :param account_identifications: The account_identifications of this Account.  # noqa: E501
        :type: list[AccountIdentification]
        """

        self._account_identifications = account_identifications

    @property
    def account_balances(self):
        """Gets the account_balances of this Account.  # noqa: E501


        :return: The account_balances of this Account.  # noqa: E501
        :rtype: list[AccountBalance]
        """
        return self._account_balances

    @account_balances.setter
    def account_balances(self, account_balances):
        """Sets the account_balances of this Account.


        :param account_balances: The account_balances of this Account.  # noqa: E501
        :type: list[AccountBalance]
        """

        self._account_balances = account_balances

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
        if not isinstance(other, Account):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Account):
            return True

        return self.to_dict() != other.to_dict()
