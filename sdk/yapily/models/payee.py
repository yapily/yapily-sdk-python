# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.264
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class Payee(object):
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
        'name': 'str',
        'address': 'Address',
        'account_identifications': 'list[AccountIdentification]',
        'merchant_id': 'str',
        'merchant_category_code': 'str'
    }

    attribute_map = {
        'name': 'name',
        'address': 'address',
        'account_identifications': 'accountIdentifications',
        'merchant_id': 'merchantId',
        'merchant_category_code': 'merchantCategoryCode'
    }

    def __init__(self, name=None, address=None, account_identifications=None, merchant_id=None, merchant_category_code=None, local_vars_configuration=None):  # noqa: E501
        """Payee - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._address = None
        self._account_identifications = None
        self._merchant_id = None
        self._merchant_category_code = None
        self.discriminator = None

        self.name = name
        if address is not None:
            self.address = address
        self.account_identifications = account_identifications
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if merchant_category_code is not None:
            self.merchant_category_code = merchant_category_code

    @property
    def name(self):
        """Gets the name of this Payee.  # noqa: E501


        :return: The name of this Payee.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Payee.


        :param name: The name of this Payee.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def address(self):
        """Gets the address of this Payee.  # noqa: E501


        :return: The address of this Payee.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Payee.


        :param address: The address of this Payee.  # noqa: E501
        :type: Address
        """

        self._address = address

    @property
    def account_identifications(self):
        """Gets the account_identifications of this Payee.  # noqa: E501


        :return: The account_identifications of this Payee.  # noqa: E501
        :rtype: list[AccountIdentification]
        """
        return self._account_identifications

    @account_identifications.setter
    def account_identifications(self, account_identifications):
        """Sets the account_identifications of this Payee.


        :param account_identifications: The account_identifications of this Payee.  # noqa: E501
        :type: list[AccountIdentification]
        """
        if self.local_vars_configuration.client_side_validation and account_identifications is None:  # noqa: E501
            raise ValueError("Invalid value for `account_identifications`, must not be `None`")  # noqa: E501

        self._account_identifications = account_identifications

    @property
    def merchant_id(self):
        """Gets the merchant_id of this Payee.  # noqa: E501


        :return: The merchant_id of this Payee.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this Payee.


        :param merchant_id: The merchant_id of this Payee.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def merchant_category_code(self):
        """Gets the merchant_category_code of this Payee.  # noqa: E501


        :return: The merchant_category_code of this Payee.  # noqa: E501
        :rtype: str
        """
        return self._merchant_category_code

    @merchant_category_code.setter
    def merchant_category_code(self, merchant_category_code):
        """Sets the merchant_category_code of this Payee.


        :param merchant_category_code: The merchant_category_code of this Payee.  # noqa: E501
        :type: str
        """

        self._merchant_category_code = merchant_category_code

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
        if not isinstance(other, Payee):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Payee):
            return True

        return self.to_dict() != other.to_dict()
